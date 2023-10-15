
import json

def transform_card_new_to_old(card):
    # 将每个卡片从新格式转换为旧格式
    return {
        "id": card.get("id"),
        "title": card.get("name") if card.get("name") else "无标题",  # 如果'name'缺失，默认为“无标题”
        "content": card.get("content"),
        "isTrashed": card.get("isTrashed", False),
        # ... 其他必要字段
    }

def transform_whiteboard_new_to_old(whiteboard):
    # 将每个白板从新格式转换为旧格式
    return {
        "id": whiteboard.get("id"),
        "name": whiteboard.get("name"),
        # ... 其他必要字段
    }

def main():
    # 加载新的数据结构
    with open('path_to_your_new_data_file.json', 'r', encoding='utf-8') as file:
        new_data = json.load(file)

    # 将新数据转换为旧格式
    old_card_list = [transform_card_new_to_old(card) for card in new_data.get("cardList", [])]
    old_whiteboard_list = [transform_whiteboard_new_to_old(whiteboard) for whiteboard in new_data.get("whiteBoardList", [])]

    # 创建旧的数据结构
    old_data_structure = {
        "cardList": old_card_list,
        "whiteBoardList": old_whiteboard_list,
        # ... 其他必要字段
    }

    # 在旧数据结构中包含新JSON数据的所有顶级键
    for key in new_data.keys():
        if key not in old_data_structure:
            old_data_structure[key] = new_data.get(key)

    # 将旧数据结构保存到JSON文件
    with open('path_to_your_converted_data_file.json', 'w', encoding='utf-8') as file:
        json.dump(old_data_structure, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
