import random

# 定義動物字典
ANIMALS = {
    1: "鯨魚",
    2: "鯊魚",
    3: "小丑魚",
    4: "旗魚",
    5: "熊貓"
}

def generate_numbers():
    """生成五個 0-5 的隨機數字"""
    return [random.randint(0, 5) for _ in range(5)]

def get_player_input():
    """獲取玩家輸入的五個數字（1-5）"""
    while True:
        try:
            numbers = input("請輸入五個數字（1-5）：")
            if len(numbers) != 5:
                print("請確實輸入5個數字！")
                continue
            numbers = [int(n) for n in numbers]
            if not all(1 <= n <= 5 for n in numbers):
                print("只能輸入1-5的數字！")
                continue
            return numbers
        except ValueError:
            print("請輸入有效的數字！")

def display_result(numbers, animals):
    """顯示水族箱中的動物"""
    result = []
    for count, animal_id in zip(numbers, animals):
        if count > 0:  # 只顯示數量大於0的動物
            result.append(f"{count}隻{ANIMALS[animal_id]}")
    return "���".join(result) + "在水族箱裡游來游去。"

def main():
    # 生成隨機數字
    random_numbers = generate_numbers()
    print(f"已生成隨機數字：{''.join(map(str, random_numbers))}")
    
    # 獲取玩家輸入
    player_numbers = get_player_input()
    
    # 顯示結果
    result = display_result(random_numbers, player_numbers)
    print(result)

if __name__ == "__main__":
    main() 