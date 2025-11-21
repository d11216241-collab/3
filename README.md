# Project Zero - 防呆計算機 / Safe Division Calculator

## 專案說明 / Project Description

這是一個實戰演練專案，目標是建立一個防呆的除法計算器，確保程式不會因「除以零」而崩潰。

This is a practical training project aimed at creating a safe division calculator that prevents crashes due to "division by zero" errors.

## 檔案結構 / File Structure

- `safe_division.py` - 主要的 safe_division 函式實作 / Main safe_division function implementation
- `test_safe_division.py` - 完整的單元測試套件 / Comprehensive unit test suite
- `demo.py` - 示範程式，展示各種使用情境 / Demo program showing various use cases
- `TEST_RESULTS.md` - 詳細的測試結果報告 / Detailed test results report

## 快速開始 / Quick Start

### 執行測試 / Run Tests

```bash
python3 -m unittest test_safe_division.py -v
```

### 執行示範程式 / Run Demo Program

```bash
python3 demo.py
```

### 使用函式 / Use the Function

```python
from safe_division import safe_division

# 正常除法 / Normal division
result = safe_division(10, 2)  # 返回 / Returns: 5.0

# 除以零（安全處理）/ Division by zero (safe handling)
result = safe_division(10, 0)  # 返回 / Returns: None
```

## 功能特色 / Features

✅ 防止除以零錯誤 / Prevents division by zero errors  
✅ 支援負數運算 / Supports negative numbers  
✅ 支援浮點數運算 / Supports floating point numbers  
✅ 完整的單元測試覆蓋 / Complete unit test coverage  
✅ 詳細的測試報告 / Detailed test reports

## 測試結果 / Test Results

查看 [TEST_RESULTS.md](TEST_RESULTS.md) 了解完整的測試結果和分析。

See [TEST_RESULTS.md](TEST_RESULTS.md) for complete test results and analysis.

## 技術規格 / Technical Specifications

- **程式語言 / Language:** Python 3.12.3
- **測試框架 / Testing Framework:** unittest
- **測試覆蓋率 / Test Coverage:** 8 test cases

## 專案任務 / Project Tasks

- [x] 任務一：撰寫防呆 safe_division 函式
- [x] 任務二：產生單元測試程式碼
- [x] 任務三：執行測試並觀察綠燈與紅燈結果

## License

MIT