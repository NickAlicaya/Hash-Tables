Open Addressing: Linear Probing
-------------------------------

One option for the project this afternoon.

  "foo" hashes to index 1
  "bar" hashes to index 2
  "baz" hashes to index 2
  "qux" hashes to index 1
  "beej" hashes to index 2

  put("foo", 12)
  put("bar", 30)
  put("baz", 99)

  get("bar")
  get("baz")

  delete("bar")

  get("baz")

  put("bar", 30)

  get("beej")

  put("baz", 88)

  put("beej", 77)

  0     1           2           3             <-- index
[ None, ("foo",12), (None,30),  ("baz",88) ]

Put:
Scan forward from the hash index until we find either the key, or None
If we find a deleted slot along the way, keep it in mind
Put the value there

Get:
Scan forward from the hash index until we find either the key, or None
Return that

Delete:
Scan forward from the hash index until we find either the key, or None
If we find the key, mark it as deleted



