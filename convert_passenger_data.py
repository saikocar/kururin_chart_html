#!/usr/bin/env python3
"""中瀬集計.xlsx の乗車人数を passenger_data.json に変換する。

使い方:
    python3 convert_passenger_data.py [xlsxパス]

xlsxパス省略時は ~/デスクトップ/中瀬集計.xlsx を読む。
出力はこのスクリプトと同じディレクトリの passenger_data.json。
AM/PM とも空欄の日は出力しない。空欄は null のまま出力する（0人と区別するため）。
"""

import datetime
import json
import sys
from pathlib import Path

import openpyxl

DEFAULT_XLSX = Path.home() / 'デスクトップ' / '中瀬集計.xlsx'
OUTPUT_JSON = Path(__file__).parent / 'passenger_data.json'

# Sheet1 の列: A=曜日, B=日付, C=乗車人数AM, D=乗車人数PM
COL_DATE, COL_AM, COL_PM = 1, 2, 3


def to_count(value):
    if value is None:
        return None
    return int(value)


def main():
    xlsx_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_XLSX
    wb = openpyxl.load_workbook(xlsx_path, data_only=True)
    ws = wb.active

    records = []
    today = datetime.date.today()
    for row_no, row in enumerate(ws.iter_rows(values_only=True), 1):
        date = row[COL_DATE]
        if not isinstance(date, datetime.datetime):
            continue
        am = to_count(row[COL_AM])
        pm = to_count(row[COL_PM])
        if am is None and pm is None:
            continue
        if date.date() > today:
            # 未来の日付は年の入力ミス（1年先に入力されている）なので前年に補正する
            corrected = date.replace(year=date.year - 1)
            print(f'補正: 行{row_no} の日付 {date:%Y-%m-%d} は未来のため {corrected:%Y-%m-%d} として扱います。')
            date = corrected
        records.append({'date': date.strftime('%Y-%m-%d'), 'am': am, 'pm': pm})

    records.sort(key=lambda r: r['date'])
    OUTPUT_JSON.write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{len(records)}日分を {OUTPUT_JSON} に書き出しました。')


if __name__ == '__main__':
    main()
