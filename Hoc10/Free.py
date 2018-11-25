import webbrowser
def getlink(i):
	ulrname={
	'Full11':'https://drive.google.com/drive/folders/1L8eieeq3w6SI5naxgZ3fUa99ilKWORrH',
	1:'https://drive.google.com/drive/folders/0ByTNUZEu-WgUT09YbW1KRVBkVTg?usp=sharing',
	2:'https://www.youtube.com/user/bsquochoai/playlists?view=50&flow=grid&shelf_id=14',
	3:'https://drive.google.com/drive/folders/1E0S4aMCdE49g_RhMz6ySDAvj33aKZMrU?usp=sharing',
	4:'https://vietjack.com/soan-van-10/index.jsp',
	5:'https://www.youtube.com/user/bsquochoai/playlists?shelf_id=12&view=50&sort=dd',
	6:'https://mega.nz/#F!UMZxmRZD!BfCllp1X1yZcDudahflNJA',
	7:'https://automatetheboringstuff.com/',
	8:'https://duolingo.com'
	}
	st=str(ulrname.get(i,0))
	return webbrowser.open(st)

print("="*40)
print("CHƯƠNG TRÌNH HỌC CHÙA".center(39, ' '))
print("="*40)
print("""1: Lý 10 GD 		2: Lý 10
3: Hóa 10		4: Soạn văn 10
5: Đại số 10 		6: TL BSQUOCHOAI
7: Học python 		8: Duolingo""")
print("="*40)

i=int(input("Nhập số thứ tự: "))
getlink(i)
