status_code =
assert status_code == 200
print("Дошли до конца")


assert status_code == 200, "Ожидали 200, получили другой код"