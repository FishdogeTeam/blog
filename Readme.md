# 前置
## 選擇與自己電腦相符系統進行下載
1. 安裝 Vscode https://visualstudio.microsoft.com/zh-hant/downloads/
2. 安裝 git https://git-scm.com/downloads
3. 安裝 node.js https://nodejs.org/zh-tw/download/

## 安裝hexo套件與blog檔案
4. 打開Vscode，點擊左上角檔案總管->開啟資料夾->選擇資料夾，到要下載檔案的資料夾
5. 上方介面點擊終端機(terminal)->新增終端 6.下方命令列(cmd)輸入 npm install -g he xo-cli
7. 下方命令列(cmd)輸入 git clone https://github.com/FishdogeTeam/blog.git
8. 下方命令列(cmd)輸入 cd blog，用意為進入blog資料夾
9. 下方命令列(cmd)輸入 npm install，系統會開始安裝相依套件 前置工作完成~~~~

# 新增作者步驟
1. 打開Vscode，點擊左上角檔案總管->開啟資料夾->選擇到blog資料夾(很重要!!!)
2. 上方介面點擊終端機(terminal)->新增終端(確認下方命令列路徑必須是在blog資料夾)
3. 左側介面點擊打開source->_authors，右鍵點擊_authors->新增檔案->取名為「作者」.yml(例:王大明.yml)
4. 點擊進入新增的作者檔案，設定name(作者名稱)、about(作者介紹)、photo(作者的照片位址)，記得冒號後面要加一個空格(很重要!!!)
5. 設定完後按下ctrl+s進行儲存
6. 下方命令列(cmd)輸入 hexo clean->輸入hexo deploy，用意為清除殘餘暫存檔案並將新增資訊部署至遠端數據儲存庫 7.到https://www.fishdogeweb.store/ 確認更新生效，部署需要一些時間，有時須等候一下

# 新增文章步驟
1. 打開Vscode，點擊左上角檔案總管->開啟資料夾->選擇到blog資料夾(很重要!!!)
2. 上方介面點擊終端機(terminal)->新增終端(確認下方命令列路徑必須是在blog資料夾)
3. 下方命令列(cmd)輸入 hexo new post 「文章名稱」
4. 左側介面點擊打開source->_posts，點擊進入剛剛新增的文章
5. 上下---之中內容為文章的設定，剛開始會幫你新增好title、date，tags(關鍵字)、authorId(作者名稱)、summary(內文預覽)、img(文章大圖位址)需自行寫入
6. tags以- 「關鍵字名稱」，重要性由上至下寫入，其餘authorId、summary、img可參考範例文章(記得冒號後面要加一個空格!!!)
7. ---下方開始撰寫文章內容，若要新增文章內圖片，語法為 「圖片名稱(自定義)」，撰寫完成後按下ctrl+s進行儲存
8. 下方命令列(cmd)輸入 hexo clean->輸入hexo deploy
9. 到https://www.fishdogeweb.store/ 確認更新生效，部署需要一些時間，有時須等候一下

# 重要事項
1. 請勿動到除了_authors和_post以外的資料夾檔案
2. 使用命令列(cmd)時請注意路徑在blog資料夾下
3. 進行作者與文章設定時，請注意冒號後面要加空格，文章內作者名稱要完全符合_authors資料夾內的作者設定
