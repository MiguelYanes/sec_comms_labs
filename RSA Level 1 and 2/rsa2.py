'''
Using the RSA values from Level 1. Can you decrypt this ciphertext?

12060751446986145559753258604964288613009905939999612142364090162932784553289274985360758786650150438909964774489580594646537566480131089578622598287608280958826485540308546699201437758196408375494069165098540792161560520821702762571130453590350894456351542803892333747581478520236785140328470857700892653885938706372579150142033036479912415927913687580857324142121399292745144946430853334522298591089627330825281302600321017113877555269059227306217943736817867883165263245345825896646180907782570834990026416074994773400197992710509066779111650705105160806274734336871715369410205954061055784649468877193662056626998

'''
import binascii

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")

with (open("rsa1.txt","r")) as f:
    for line in f:
        letter = line[0]
        if letter == 'n':
            n = int(line[3:])
        elif letter == 'e':
            e = int(line[3:])
        elif letter == 'd':
            d = int(line[3:])
        elif letter == 'p':
            p = int(line[3:])
        elif letter == 'q':
            q = int(line[3:])

ciphertext = 12060751446986145559753258604964288613009905939999612142364090162932784553289274985360758786650150438909964774489580594646537566480131089578622598287608280958826485540308546699201437758196408375494069165098540792161560520821702762571130453590350894456351542803892333747581478520236785140328470857700892653885938706372579150142033036479912415927913687580857324142121399292745144946430853334522298591089627330825281302600321017113877555269059227306217943736817867883165263245345825896646180907782570834990026416074994773400197992710509066779111650705105160806274734336871715369410205954061055784649468877193662056626998

decrypted = pow(ciphertext, d, n)   ## decrypt
plaintext = int2string(decrypted)
print ("Decrypyed message: " + str(plaintext))

