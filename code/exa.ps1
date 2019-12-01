# エクササイズA2: パス、フォルダ、ディレクトリ (pwd)
cd ~
pwd


# エクササイズA3: もし迷子になったら
cd ~
pwd
cd ~


# エクササイズA4: ディレクトリを作成する (`mkdir`)
cd ~  # ホームディレクトリに戻る

pwd
cd ~
mkdir clcc
mkdir clcc/stuff
mkdir clcc/stuff/things
mkdir clcc/stuff/things/orange/apple/pear/grape


# エクササイズA5: ディレクトリを移動する (`cd`)
cd ~

cd clcc
pwd
cd stuff
pwd
cd things
pwd
cd orange
pwd
cd apple
pwd
cd pear
pwd
cd grape
pwd
cd ..
cd ..
pwd
cd ..
cd ..
pwd
cd ../../..
pwd
cd clcc/stuff/things/orange/apple/pear/grape
pwd
cd ../../../../../../../
pwd


# エクササイズA6: ディレクトリを一覧表示する (`ls`)
cd ~

cd clcc
ls
cd stuff
ls
cd things
ls
cd orange
ls
cd apple
ls
cd pear
ls
cd grape
ls
cd ..
ls
cd ../../..
ls
cd ../..
ls


# エクササイズA7: ディレクトリを削除する (`rmdir`)
cd ~

cd clcc
ls
cd stuff/things/orange/apple/pear/grape/
cd ..
rmdir grape
cd ..
rmdir pear
cd ..
ls
rmdir apple
cd ..
ls
rmdir orange
cd ..
ls
rmdir things
cd ..
ls
rmdir stuff
pwd
cd ..


# エクササイズA8: ディレクトリをあちこち移動する (`pushd`, `popd`)
cd ~

cd clcc
mkdir i/like/icecream
pushd i/like/icecream
popd
pwd
pushd i/like
pwd
pushd icecream
pwd
popd
pwd
popd

rm -r ~/clcc/i  # 次のエクササイズに進む前にi/like/icecreamディレクトリは削除しておく


# エクササイズA9: 空のファイルを作成する (`touch`/`new-item`)
cd ~

cd clcc
new-item iamcool.txt -type file
ls


# エクササイズA10: ファイルをコピーする (`cp`)
cd ~

cd clcc
cp iamcool.txt neat.txt
ls
cp neat.txt awesome.txt
ls
cp awesome.txt thefourthfile.txt
ls
mkdir something
cp awesome.txt something/
ls
ls something
cp -r something newplace
ls newplace


# エクササイズA11: ファイルを移動する (`mv`)
cd ~

cd clcc
mv awesome.txt uncool.txt
ls
mv newplace oldplace
ls
mv oldplace newplace
ls newplace
ls


# エクササイズA12: ファイルの中身を見る (`less`/`more`)
cd ~

# ... テキストエディタを使ってデスクトップにtest.txtを作成する ...
cd clcc
cp ~/Desktop/test.txt .
more test.txt


# エクササイズA13: ファイルの内容を表示する (`cat`)
cd ~

# ... テキストエディタを使ってclccに直接test2.txtを作成する ...
cd clcc
more test2.txt
cat test2.txt
cat test.txt

rm test.txt test2.txt  # 次のエクササイズに進む前にtest.txtとtest2.txtファイルを削除しておく


# エクササイズA14: ファイルを削除する (`rm`)
cd ~

cd clcc
ls
rm uncool.txt
ls
rm iamcool.txt
rm neat.txt
rm thefourthfile.txt
ls
cp -r something newplace
rm something/awesome.txt
rmdir something
rm -r newplace
ls


# エクササイズA15: ターミナルを終了する (`exit`)
cd ~

exit
