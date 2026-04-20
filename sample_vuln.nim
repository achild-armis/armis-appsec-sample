import strutils

proc buildLoginQuery(username, password: string): string =
  # Vulnerable: directly concatenates untrusted input into SQL
  result = "SELECT * FROM users WHERE username = '" &
           username & "' AND password = '" & password & "'"

when isMainModule:
  let username = "admin' --"
  let password = "anything"
  echo buildLoginQuery(username, password)
