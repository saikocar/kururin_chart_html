# kururin_chart_html

くるりん自動運転のデータを可視化するチャートHTMLファイル集

## 公開先

- **本番**: https://sites.google.com/view/kururin-jidouunten
- **デバッグ用**: https://sites.google.com/view/kururin-jidouunten-debug
  - デバッグ用サイトには、何らかの問題やデバッグが必要と考えられるデータ・グラフを掲載しています

## ファイル構成

| ファイル | 説明 |
|---------|------|
| autonomous_data.json | 自動運転データ（JSON形式） |
| autonomy_rate.html | 自律率グラフ |
| brake_count.html | ブレーキ回数グラフ |
| cmd_brake.html | コマンドブレーキグラフ |
| delay.html | 遅延グラフ |
| guidance_error.html | 誘導誤差グラフ |
| intervention_brake.html | 介入ブレーキグラフ |
| intervention_rate.html | 介入率グラフ |
| intervention_rate_with_gaspedal.html | アクセル介入率グラフ |
| mrm.html | MRMグラフ |
| unnecessary_brake.html | 不要ブレーキグラフ |

## 開発フロー

### リポジトリ構成

- `origin`: 自分のフォーク（DWatabe/kururin_chart_html）
- `upstream`: 本家リポジトリ（saikocar/kururin_chart_html）

### 変更を反映する手順

1. ブランチで作業
   ```bash
   git checkout -b feature/your-feature
   ```

2. 変更をコミット
   ```bash
   git add <変更ファイル>
   git commit -m "変更内容の説明"
   ```

3. originにプッシュ
   ```bash
   git push origin feature/your-feature
   ```

4. upstreamへプルリクエスト(PR)を作成
   - GitHub上でsaikocar/kururin_chart_htmlに対してPRを作成

### upstreamの変更を取り込む

```bash
git fetch upstream
git merge upstream/main
```
