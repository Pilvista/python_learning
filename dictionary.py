monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    0: "Nolla",
    1: "Yksi",
    2: "Kaski"
}

print(monthConversion["Oct"])
print(monthConversion.get("Dec"))
print(monthConversion.get(1))
