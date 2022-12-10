hexo g
git add .
git commit -m "更新文章"
git push

git checkout gh_pages

mv public/ ..
mv node_modules ..
mv .git ..
mv .gitignore ..
rm -rf *
echo "test.fishdogeweb.store" > CNAME
mv ../public/* .
mv ../node_modules .
mv ../.git .
mv ../.gitignore .
rm -rf ../public
git add .
git commit -m "更新文章"
git push
