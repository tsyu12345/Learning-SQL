SELECT Title as title, ArtistId as id --列指定
/*[ as ]でカラムに別名を付けて表示することも可能*/
FROM albums --テーブル名
WHERE ArtistId!= 2 --抽出するレコードの条件
ORDER BY ArtistId, title ASC
--ORDER BY id DESC
/*asで付けた別名で行うソートする事も可能*/
/*
* ORDER BY [ソート基準にしたいカラム名], ...
* ASC : 昇順
* DESC: 降順
*/