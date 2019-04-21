# Lab 2B - Classic Ciphers in the Command Line
# Rot 5
echo "Out digits are: 56789" > digits.txt
cat digits.txt
echo " - Apply ROT 5:"
cat digits.txt | tr [0-9] [5-90-4]

echo "--------------------------------"

# Rot 13
echo "EBG 13 JNF HFRQ OL ZVPEBFBSG SBE RAPBQVAT JVAQBJF ERTVFGELRAGEVRF" > rot13.txt
cat rot13.txt
echo " - Apply ROT 13:"
cat rot13.txt |  tr [A-Z] [N-ZA-M]

echo "--------------------------------"

# Caesar's Cipher
echo "Wkh ruljlqdo Fdhvdu flskhu dozdBv xvhg d vkliw ri wkuhh" > caesar.txt
cat caesar.txt
echo " - Decode Casar Cipher"
cat caesar.txt | tr [a-z][A-Z] [x-za-w][X-ZA-W]

echo "--------------------------------"

# Rot 47
echo "(:E9 6IA6C:6?46 J@F H:== DE2CE E@ C64@8?:D6 E96 492C24E6C D6ED @7 6249 6?4@5:?8]" > rot47.txt
cat rot47.txt
echo " - Decode ROT 47:"
cat rot47.txt | tr ‘\!-~’ ‘P-~\!-O’

echo "--------------------------------"

# Alias
alias rot5='tr [0-9] [5-90-4]'
alias rot13='tr [A-Z] [N-ZA-M]'
alias deccaesar='tr [a-z][A-Z] [x-za-w][X-ZA-W]'
alias rot47='tr ‘\!-~’ ‘P-~\!-O’'

cat digits.txt | rot5
cat rot13.txt | rot13
cat caesar.txt | deccaesar
cat rot47.txt | rot47