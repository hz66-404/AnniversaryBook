#!/usr/bin/env python3
"""
批量将 HEIC 图片转换为 PNG 格式
"""

import os
import sys
from pathlib import Path

try:
    from PIL import Image
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    print("错误: 需要安装必要的库")
    print("请运行以下命令安装:")
    print("pip install pillow pillow-heif")
    sys.exit(1)

def convert_heic_to_png(folder_path):
    """
    将文件夹中的所有 HEIC 文件转换为 PNG
    
    Args:
        folder_path: 文件夹路径
    """
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"错误: 文件夹不存在: {folder_path}")
        return
    
    # 查找所有 HEIC 文件
    heic_files = list(folder.glob("*.heic")) + list(folder.glob("*.HEIC"))
    
    if not heic_files:
        print(f"在 {folder_path} 中没有找到 HEIC 文件")
        return
    
    print(f"找到 {len(heic_files)} 个 HEIC 文件")
    print("-" * 50)
    
    converted_count = 0
    failed_count = 0
    
    for heic_file in heic_files:
        try:
            # 生成 PNG 文件名
            png_file = heic_file.with_suffix('.png')
            
            print(f"转换: {heic_file.name} -> {png_file.name}")
            
            # 打开 HEIC 并保存为 PNG
            img = Image.open(heic_file)
            img.save(png_file, 'PNG')
            
            converted_count += 1
            print(f"  ✓ 成功")
            
        except Exception as e:
            failed_count += 1
            print(f"  ✗ 失败: {str(e)}")
    
    print("-" * 50)
    print(f"转换完成:")
    print(f"  成功: {converted_count} 个")
    print(f"  失败: {failed_count} 个")
    
    if converted_count > 0:
        print(f"\nPNG 文件已保存在: {folder}")

def main():
    # 默认使用当前脚本所在的文件夹
    folder_path = Path(__file__).parent
    
    # 如果提供了命令行参数，使用指定的文件夹
    if len(sys.argv) > 1:
        folder_path = Path(sys.argv[1])
    
    print(f"转换文件夹: {folder_path}")
    print()
    
    convert_heic_to_png(folder_path)

if __name__ == "__main__":
    main()
