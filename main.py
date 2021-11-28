from foo.group.group import get_reader as get_group_reader
from foo.filter.filterchain import FilterChain
from foo.option.option import get_handler
from foo.conf.yaml_parse import get_config
from foo.importer.reader import importer
from foo.outputer.writer import outputer
from foo.appender.appender import appender

# 处里输入信息
def handle_inputs(config):
    datas = {}
    for x in config:
        input_map = handle_inputer(x)
        datas[x["name"]] = input_map
    return datas
        

# 处理单项输入信息
def handle_inputer(inputer):
    input_map = {}
    outters = inputer["outters"]
    for o in outters:
        group_map = handle_outter(inputer, o)
        # df = pd.DataFrame.from_dict(group_map, orient="index")
        input_map[o["name"]] = group_map
    return input_map

# 处理单个输入项
def handle_outter(inputer, outter):
    reader = importer(inputer["type"])
    reader.load({
        "path": inputer["value"],
    })
    group_info = outter["group"]
    group_reader = get_group_reader(group_info["handler"])
    group_reader.load(group_info["param"])
    filter_chain = FilterChain()
    for x in outter["filters"]:
        filter_chain.add(x)
    size = reader.get_size()
    group_map = {}
    for x in range(size):
        row = reader.get_row(x)
        if not filter_chain.do_filter(row):
            continue
        group_name = group_reader.get(reader.get_value(group_info["column"], x))
        if group_name not in group_map:
            group_map[group_name] = {
                "group": group_name,
            }
        group_data = group_map[group_name]
        for o in outter["options"]:
            get_handler(o["type"]).handle(row, o, group_data)
    return group_map


# 输出全部数据
def handle_outputs(datas, config):
    for x in config:
        handle_output(datas, x)

# 输出单个数据
def handle_output(datas, output):
    writer = outputer(output["type"])
    writer.load(output)
    appender_cfg = output["appender"]
    append = appender(appender_cfg["name"])
    df = append.append(datas, appender_cfg)
    writer.wirte(df)
    pass

def main():
    config = get_config('conf/config.yaml')
    input_cfg = config["input"]
    datas = handle_inputs(input_cfg)
    output_cfg = config["output"]
    handle_outputs(datas, output_cfg)
    print(datas)

'''
# 执行入口
'''
if __name__ == '__main__':
    main()
