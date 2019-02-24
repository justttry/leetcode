#encoding:UTF-8
#author:justry

# Definition for singly-linked list.

import random
import collections
import time

class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letterDict = collections.defaultdict(set)
        for i, j in enumerate(words):
            for k in j:
                letterDict[k].add(i)
        seen = set()
        whole = set(range(len(words)))
        ret = 0
        for i, j in enumerate(words):
            length = len(j)
            seen.add(i)
            intersect = set()
            for k in j:
                intersect = intersect.union(letterDict[k])
            unseen = whole - seen - intersect
            for k in unseen:
                a = length * len(words[k])
                ret = max(ret, a)
        return ret

startTime = time.time()
a = Solution()
data = ["abcw","baz","foo","bar","xtfn","abcdef"]
b = a.maxProduct(data)
print(b)
print(time.time()-startTime)

startTime = time.time()
a = Solution()
data = ["ecdhogacblkfkpdkddpjcogpgin","ifo","abmcenkaijglaf","baeiacagkiciokbg","gcbpjegofjbcencpeglbaabe","lemekpgmeljhcnhknigangmhhleipoagpgmdipicjnojfpef","calojonebkipbdnlokallgpigno","ppddceokpahljijkklbimihmkfdnki","eecbnbmoaifm","jnpoonkmeafbmn","nihimflkgdgmhdlimgh","aabljdkhgmilnhopcdfdedkmiecjeghecjaoknkggongmddagn","ckabnbliklicbmcfgcpkhenchkcjkdkkkd","cojhfpngcloadgpmdopkjbjckko","olplcaljidkb","bo","echhpckfcplkfmocgnafjegmhbolgajlcidpmmop","kblaellmglcjhfbkeiboa","lmkllognlpcdcfceepdiakebhelmgglaihfnjglbiplfkkjg","eogaoanhjoamndgpkcomacogelkodillamoibjbippgflaiap","ohpm","jhcgjadghocikhgiponodbb","loflhhkmeimioomhnfpibagpmalkfkfckjejnkogblbcgmn","fakpoflmhgjgpjhmin","pcblmfoehecdbljllabbbgdddmemjj","baoodangefnhnkolecncjeolgeepkkgdnbgphkkg","mgodiaodpbbenllnd","gdpfca","iebadcihnojoedhdghnpbalgepbpjhlnpcebhhakk","mnejbdhocpcjbipdanbefmihpf","nodhfbphicmbnfnniphmmogege","lopbm","ifdjbbnojijfkdembdaibobdejmdncfkid","fcpaekcdcbghdgdmjchiebikkpol","dbefd","cnkmjojekjnompmhfafopof","hk","mikpjdfd","hoipdbgficoljhanalfplgpegcchfefamoanege","cnffbmbnhaeeoliochnfjbpbfbfkckk","dfnfji","amcgfkjfhojhhdmgkejgnknbjfmlcjjegceoacg","apjlffmikbaoagpbocdmpnbf","iiafc","dleofdplcdgdah","lfooapipalbeincogndoiceciboajnofejklheggfmeahbpfpc","kk","monongehinlkbikaadgpnegagonfcjanlmgkblmobegfhffpio","cipopjlboe","oahkona","aeagbfoffklkkadjmbmogolpibgmiinlecpglck","cbbfmhgobjjgkchmiiggjcekjeeehcpdbbj","gcnlllnecfkoheahbcdkicmjbeihjecjdjmghjgfge","glphjnlgpnoklgpbjhapicgcgkmiolggdafeojck","njgdgagjjejneohkbicglbjmliehcdkjldf","hmpanoohkjplmpknbeha","nbkffamaehdagmoaomeklcbppmnnmfjdmihfjkdohjkf","cddogapgddmgoggfnalcofklnepciinbcagkmaobmfaockfpk","aelfgmnilmciimpemogocbnkgog","kokjepkjhnfiijglafggpbilabcjoc","aljgd","omnogphbciplabjfdemnannbp","agecffmibopappodjopcalhg","iojlipfbdfllbniidpefmlfjcebnhmedilpkalpmoepnjbeim","nicifkaflhcjodejah","eoifklfbkjlgibjfpdkjahkfglefooipeelfkghkhk","jjpejngcfapcmeoiemhpdn","cmdmjgieapomg","ppgaljpdkadbdolpdmj","cfbjncidookaiapdbjpgflfmoeeihkniafkolflbnllmn","mobdldhadjk","jkehgchaaljbajkjc","eiek","ocnimglgblfelmfjeoalplfdnjdefjnm","hmfogclggljldnlfdhbjkdipbnkokedc","diclfepjagmojiam","phkadblgokgebpfdpllcikkfopceagnebcn","jmbbpb","maneopbjcchanokdlcbkdffpeaebcoaicohhognoffeodo","njfnpkbigejf","mogmbbalpjminchicaigokpnolj","eagekfmekeminhdpodkelfillkgnbchdk","oaobfgacioflban","lcligbbpfejnjnkglemabbdnabigeaaogne","fclbhhkmacbhffbklbhfcdefhgbmadpdhepodhhbimcbjljaea","gfecjgjiejnofialaapnpaeljfiokjoipeipjmjikghc","apibjlgenhnacmelpnfhbmbphkcipefgfingbionoipjbfbebik","eioglhippcaglbllepimfpmckbeeoopapncbbpjbpladmekemb","dhnkpoen","ojlddlkpehejeiepglfc","emkokalhdgejfhioolaflbgd","jiliiniahldmojakpoifmhfhlciddjkipbbgaolniidp","idnmb","ogeldppjjbeaafamljefaimmdgaf","njggccdbbcjkcgimjclabbaldbcc","ipcegcmpojmnnkhhemdh","bfjjmijcmebifmeoenpealepceehmmjppeljgmgekgknbpp","ddegchbpejigfillkngkncljjgpidonnck","cbpjimih","liddojcamngloafnoacclfhldiofncldgog","jbggofoojoaljmalfgi","holcklaloohpfjnifnebjhhjnkchkkok","facacencgieblepkjppnlolabglgnpiehakpnl","mpgkklnfl","dbffpgac","eiflmnbecdodgdfomaeb","ghadkfoicddjofgpkcfikdhmoplfofepbaa","afioff","dlcfnheplnompahgailjnabfih","iancmadnbmghfhgidlaofpckkacfbdgadpafbcjb","ciopmankgkpbkpdmhicdncknlnbnndnghnflcdo"]
b = a.maxProduct(data)
print(b)
print(time.time()-startTime)