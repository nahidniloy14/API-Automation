#Delete Book
import requests

deleteBook=requests.post("http://216.10.245.166/Library/DeleteBook.php",json={
    "ID":"gagfksgkaf"

})
assert deleteBook.status_code == 200
print(deleteBook)
#{msg: book is successfully deleted”}
