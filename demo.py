"""
示範程式 / Demo Program
展示 safe_division 函式的使用方法
Demonstrates how to use the safe_division function
"""

from safe_division import safe_division


def main():
    print("=" * 60)
    print("Project Zero - 防呆計算機示範 / Safe Division Calculator Demo")
    print("=" * 60)
    print()
    
    # 測試案例 / Test cases
    test_cases = [
        (10, 2, "正常除法 / Normal division"),
        (100, 4, "整數除法 / Integer division"),
        (7, 2, "小數結果 / Decimal result"),
        (-10, 2, "負數除法 / Negative division"),
        (10, -2, "除以負數 / Divide by negative"),
        (-10, -2, "負負得正 / Negative divided by negative"),
        (10, 0, "除以零（防呆）/ Division by zero (safe)"),
        (0, 5, "零除以數 / Zero divided by number"),
        (10.5, 2.5, "浮點數除法 / Floating point division"),
    ]
    
    for a, b, description in test_cases:
        result = safe_division(a, b)
        print(f"{description}")
        print(f"  {a} ÷ {b} = {result}")
        
        if result is None:
            print(f"  ⚠️  防呆機制啟動：避免了除以零的錯誤！")
            print(f"  ⚠️  Safety mechanism activated: Prevented division by zero error!")
        print()
    
    print("=" * 60)
    print("✅ 所有計算完成，程式沒有崩潰！")
    print("✅ All calculations completed without crashes!")
    print("=" * 60)


if __name__ == "__main__":
    main()
