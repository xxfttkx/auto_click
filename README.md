# auto_click

活下去，星痕共鸣

## 📦 安装依赖

首先确保你已安装 Python 3.7 及以上版本，然后安装依赖：

```bash
pip install -r requirements.txt
```

## 🚀 使用方法

运行脚本：

```bash
python main.py [--method {postMessage,pygetwindow}] [--interval 秒数]
```

### 参数说明

| 参数         | 说明                                           | 默认值        |
| ------------ | ---------------------------------------------- | ------------- |
| `--method`   | 点击方法，可选：`postMessage` 或 `pygetwindow` | `pygetwindow` |
| `--interval` | 每次点击之间的时间间隔（单位：秒）             | `37` 秒       |

### 示例

```bash
# 使用默认方式 pygetwindow，每 37 秒点击一次
python main.py

# 使用 postMessage，每 18 秒点击一次
python main.py --method postMessage --interval 18
```

## 🛠️ 支持的方法说明

- `pygetwindow`：通过控制窗口与模拟鼠标点击完成操作。
- `postMessage`：通过 Windows API 向窗口发送点击消息。

## 📝 注意事项

- 部分方法可能需要以管理员权限运行脚本。

## 开发过程

[《星痕共鸣》自动采集](https://xxfttkx.github.io/p/%E6%98%9F%E7%97%95%E5%85%B1%E9%B8%A3%E8%87%AA%E5%8A%A8%E9%87%87%E9%9B%86/)
