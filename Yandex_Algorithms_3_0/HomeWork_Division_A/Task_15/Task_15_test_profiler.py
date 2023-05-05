# https://contest.yandex.ru/contest/45469/problems/15/
# Дивизион A
# 15. Поврежденный XML
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        xml_string = file.readline().strip()
    return xml_string


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Корректировка XML
def correct_xml(xml_string):
    '''
    входные данные
    :xml_string — исходная XML строка которую надо скорректировать

    выходные данные
    :valid_xml — итоговая XML строка, с исправленными ошибками
    '''
    stack = []

    def addition_tag(start_pos, end_pos):
        print(f"addition_tag, start_pos: {start_pos}, end_pos: {end_pos}, sub: {xml_string[start_pos:end_pos]}")

        if end_pos == len(xml_string) - 1:
            end_pos = len(xml_string)
        print(f"end_pos: {end_pos}")
        print(f"addition_tag 1: start_pos:{start_pos}, end_pos: {end_pos}")
        tag = xml_string[start_pos:end_pos]
        print(tag)
        check_tag = True
        if tag[1] != "/":
            stack.append([tag, (start_pos, end_pos)])
            check_tag = True
        elif tag[1] == "/":
            if len(stack) == 0:
                # Эта ситуация как раз говорит о том что первый тэг стоит как закрывающий, но мы все-равно помечаем,
                # что все хорошо, чтобы произошло добалвение следующего тэга
                stack.append([tag, (start_pos, end_pos)])
                check_tag = True
            elif stack[-1][0] == tag.replace("/", ""):
                stack.pop()
                check_tag = True
            else:
                print(f"Find error tag: {tag}, {stack[-1][0]}")
                stack.append([tag, (start_pos, end_pos)])
                # Не всегда проблема может быть именно в последних двух бывает, что и у предпоследних двух, например
                # <l><it><wit></l>, поэтому требуется дополнительная проверка
                for item in stack:
                    if item[0] == tag.replace("/", ""):
                        stack.pop()
                        break
                check_tag = False
        print(f"stack: {stack}, check_tag: {check_tag}")
        if not check_tag and len(stack[-2][0]) != len(stack[-1][0]) -1:
            stack.pop()
            return None
        return check_tag

    def find_change_symbol(open_tag_pos, close_tag_pos):
        print(f"open_tag_pos:{open_tag_pos}, close_tag_pos: {close_tag_pos}")
        open_tag = xml_string[open_tag_pos[0]: open_tag_pos[1]]
        close_tag = xml_string[close_tag_pos[0]: close_tag_pos[1]]
        print(f"open_tag 2: {open_tag}, close_tag: {close_tag}")
        if open_tag[0] != '<':
            return (open_tag_pos[0], open_tag_pos[0] + 1, "<")
        elif open_tag[-1] != '>':
            return (open_tag_pos[1] - 1, open_tag_pos[1], ">")
        elif close_tag[0] != '<':
            return (close_tag_pos[0], close_tag_pos[0] + 1, "<")
        elif close_tag[1] != '/':
            return (close_tag_pos[0] + 1, close_tag_pos[0] + 2, "/")
        elif close_tag[-1] != '>':
            return (close_tag_pos[1] - 1, close_tag_pos[1], ">")
        elif open_tag[1:-1] != close_tag[2:-1]:
            # Нужно выбрать какой именно тэг брать за основу, главное чтобы там были буквы, а не спецсимволы "</>"
            print(f"close_tag[2:-1]: {close_tag[2:-1]}")
            print(f"close_tag[2:-1]: {close_tag[2:-1]}")
            print(f"open_tag[1:-1]: {open_tag[1:-1]}")
            print(f"open_tag[1:-1].isalpha(): {open_tag[1:-1].isalpha()}")
            if close_tag[2:-1].isalpha():
                return (open_tag_pos[0] + 1, open_tag_pos[-1] - 1, close_tag[2:-1])
            else:
                return (close_tag_pos[0] + 2, close_tag_pos[-1] - 1, open_tag[1:-1])

    print(xml_string)
    start_pos = end_pos = 0
    open_tag = True
    check_tag = True
    for idc in range(1, len(xml_string)):
        char = xml_string[idc]
        print(f"char:{char}, start_pos: {start_pos}, end_pos:{end_pos}")
        if char == "<" and not open_tag:
            start_pos = idc
            open_tag = True
        elif char == "<" and open_tag:
            print(f"char == '<' and open_tag")
            print(f"start_pos: {start_pos}, end_pos:{end_pos}")
            print(f"xml_string[idc - 1]: {xml_string[idc - 1]}")
            if idc == len(xml_string) - 1:
                end_pos = idc
                open_tag = False
                print(f"xml_string 1: '{xml_string[start_pos:end_pos]}' start_pos: {start_pos}, end_pos:{end_pos}")
                check_tag = addition_tag(start_pos, end_pos)
            elif xml_string[idc - 1] == "<" or xml_string[idc - 1] == ">":
                print(f"--------------- xml_string[idc - 1] == '<'")
                pass
            elif xml_string[idc + 1] == "<":
                end_pos = idc + 1
                open_tag = False
                print(f"xml_string 2: '{xml_string[start_pos:end_pos]}' start_pos: {start_pos}, end_pos:{end_pos}")
                check_tag = addition_tag(start_pos, end_pos)
                print(f"check_tag: {check_tag}")
                if check_tag is not None:
                    start_pos = idc + 1
            elif xml_string[idc + 1] == ">":
                end_pos = idc + 2
                open_tag = False
                print(
                    f"xml_string __2.5__: '{xml_string[start_pos:end_pos]}' start_pos: {start_pos}, end_pos:{end_pos}")
                check_tag = addition_tag(start_pos, end_pos)
                print(f"check_tag: {check_tag}")
                if check_tag is not None:
                    start_pos = idc + 2
            elif xml_string[idc + 1] != "<":
                end_pos = idc
                open_tag = True
                print(f"xml_string 3: '{xml_string[start_pos:end_pos]}' start_pos: {start_pos}, end_pos:{end_pos}")
                check_tag = addition_tag(start_pos, end_pos)
                print(f"check_tag: {check_tag}")
                if check_tag is not None:
                    start_pos = idc
            print(f"xml_string 4: '{xml_string[start_pos:end_pos]}' start_pos: {start_pos}, end_pos:{end_pos}")
        elif char == ">" and check_tag is None:
            end_pos = idc + 1
            check_tag = addition_tag(start_pos, end_pos)
            start_pos = end_pos + 1
        elif char == ">" and not open_tag and xml_string[idc - 1] == ">":
            print("char == ">" and not open_tag")
            start_pos = idc
            open_tag = True
        elif char == ">" and open_tag and xml_string[idc - 1] != "<":
            print(f"elif char == " > " and open_tag:")
            end_pos = idc
            open_tag = False
            check_tag = addition_tag(start_pos, end_pos + 1)
            if check_tag is not None:
                start_pos = end_pos + 1

        elif idc == len(xml_string) - 1:
            check_tag = addition_tag(start_pos, idc + 1)
            print(f"check_tag 5: {check_tag}")
        if not check_tag and check_tag is not None:
            break
    if not check_tag or len(stack) != 0:
        print(f"check_tag 3: {check_tag} len(stack): {len(stack)}")
        open_tag_start = stack[-2][1][0]
        open_tag_end = stack[-2][1][1]
        close_tag_start = stack[-1][1][0]
        close_tag_end = stack[-1][1][1]

        open_tag = xml_string[open_tag_start: open_tag_end]
        close_tag = xml_string[close_tag_start:close_tag_end]

        print(f"open_tag 1: {open_tag}, close_tag: {close_tag}")
        change_char = find_change_symbol((open_tag_start, open_tag_end), (close_tag_start, close_tag_end))
        print(f"change_char: {change_char}")
        list_xml = list(xml_string)
        list_xml[change_char[0]: change_char[1]] = list(change_char[2])
        valid_xml = "".join(list_xml)
        print(f"valid_xml: {valid_xml}")
        return valid_xml

    return xml_string


def main():
    # считываем входные данные
    xml_string = load_data(INPUT_FILE)
    # Корректировка XML
    valid_xml = correct_xml(xml_string)
    print(f"valid_xml: {valid_xml}")
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, valid_xml)


import pytest


@pytest.mark.parametrize(
    "xml_string, target_valid_xml",
    [
        # ("", ""),
        # ("", ""),
        ("<crthf><unex><cu><n><x><hddts></hddts><uo></uo></x><a></a>>pims></pims></n><bwnr><n></n><mbh><oxip></oxip></mbh><l><zsll></zsll></l><wkm></wkm></bwnr><fupy><n></n><tzwz></tzwz></fupy><c></c><zdcf></zdcf></cu><mnmiy><erbs><blbrs></blbrs><dht></dht><pfkn></pfkn><mbjz></mbjz><nn></nn></erbs><cju><wbapi></wbapi></cju><q><szfgb></szfgb><qhxr></qhxr></q><k></k><lgt></lgt></mnmiy><m><jrop><kko><jo></jo><kyju></kyju></kko><xi></xi><ezq></ezq></jrop><lif><zatch></zatch></lif><aacu></aacu><h></h><z></z></m><yfl><exvlh><rspia></rspia><xo><rsqgq></rsqgq><eb></eb></xo><rg></rg></exvlh><riakg></riakg></yfl><hjy></hjy></unex><oq></oq><yofe><u></u><fuvda></fuvda><a></a></yofe><chcyp></chcyp></crthf><meph></meph><qc><prg></prg></qc><x><lrn></lrn></x><ern></ern>", "<crthf><unex><cu><n><x><hddts></hddts><uo></uo></x><a></a><pims></pims></n><bwnr><n></n><mbh><oxip></oxip></mbh><l><zsll></zsll></l><wkm></wkm></bwnr><fupy><n></n><tzwz></tzwz></fupy><c></c><zdcf></zdcf></cu><mnmiy><erbs><blbrs></blbrs><dht></dht><pfkn></pfkn><mbjz></mbjz><nn></nn></erbs><cju><wbapi></wbapi></cju><q><szfgb></szfgb><qhxr></qhxr></q><k></k><lgt></lgt></mnmiy><m><jrop><kko><jo></jo><kyju></kyju></kko><xi></xi><ezq></ezq></jrop><lif><zatch></zatch></lif><aacu></aacu><h></h><z></z></m><yfl><exvlh><rspia></rspia><xo><rsqgq></rsqgq><eb></eb></xo><rg></rg></exvlh><riakg></riakg></yfl><hjy></hjy></unex><oq></oq><yofe><u></u><fuvda></fuvda><a></a></yofe><chcyp></chcyp></crthf><meph></meph><qc><prg></prg></qc><x><lrn></lrn></x><ern></ern>"),
        ("<crthf><unex><cu><n><x><hddts></hddts><uo></uo></x><a></a>>pims></pims>", "<crthf><unex><cu><n><x><hddts></hddts><uo></uo></x><a></a><pims></pims>"),
        ("<v><lilxi><cjejt></cjejt></li>xi></v>", "<v><lilxi><cjejt></cjejt></lilxi></v>"),
        ("<q><m></m><t><mtg></mtg></t><ew></e<></q>", "<q><m></m><t><mtg></mtg></t><ew></ew></q>"),
        ("<l><it><wit></l>", "<l><it></it></l>"),
        (
                "<v><tbvh></tbvh><o><kksav></kksav></o><ypya></ypya><saed></saed><urgps></urgps></v><bdf><kgls><h></h></kgls><af><yv></yv></af><bxf></bxf></bdf><is></is><od></od<",
                "<v><tbvh></tbvh><o><kksav></kksav></o><ypya></ypya><saed></saed><urgps></urgps></v><bdf><kgls><h></h></kgls><af><yv></yv></af><bxf></bxf></bdf><is></is><od></od>"),
        ("<b>./b>", "<b></b>"),
        ("</d></ad>", "<ad></ad>"),
        ("</></a>", "<a></a>"),
        (
                "<kycvu><q><lfnc><pddhl><kcu><kyy></kyy><y><bia><ukhq></ukhq><pspuc></pspuc></bia><q></q></y><udj></udj></kcu><kvmha><bgif></bgif></kvmha><qjn><bp></bp></qjn><tzui></tzui><el></el></pddhl><ddr></ddr><adee></adee><mvn></mvn><rd></rd></lfnc><qrnb></qrnb></q><j></j><kvhs></kvhs><z></z></kycvu><eetup></eetup><n><cgb><kjbz><a></a></vjbz><msip></msip><eq></eq><qgtf></qgtf></cgb><dkjtd></dkjtd><e></e></n><enl></enl>",
                "<kycvu><q><lfnc><pddhl><kcu><kyy></kyy><y><bia><ukhq></ukhq><pspuc></pspuc></bia><q></q></y><udj></udj></kcu><kvmha><bgif></bgif></kvmha><qjn><bp></bp></qjn><tzui></tzui><el></el></pddhl><ddr></ddr><adee></adee><mvn></mvn><rd></rd></lfnc><qrnb></qrnb></q><j></j><kvhs></kvhs><z></z></kycvu><eetup></eetup><n><cgb><vjbz><a></a></vjbz><msip></msip><eq></eq><qgtf></qgtf></cgb><dkjtd></dkjtd><e></e></n><enl></enl>"),
        ("<a/</a>", "<a></a>"),
        ("<a><>a>", "<a></a>"),
        ("<a><ab></ab><c></c></a>", "<a><ab></ab><c></c></a>"),
        ("<dz><ddz>", "<dz></dz>"),
        ("<<z></iz>", "<iz></iz>"),
        ("<izd</iz>", "<iz></iz>"),
        ("<sz></iz>", "<iz></iz>"),
        ("<a></b>", "<b></b>"),
        ("piz></iz>", "<iz></iz>"),
        (
                "<i><zgpvh><u><w></w></u><rcojp><mkqg></mkqg></rcojp><y></y></zgpvh><jsbqa></jsbqa></i><vwi><xpv><bdn><lvd><u></u><rb><zza></zza></rb><brjca></brjca></lvd><s><tchq><ya></ya><lb><d></d><tkav></tkav><uxfr><g></g></uxfr><vv></vv></lb><te></te><ooq><c></c></ooq><kirpl></kirpl></tchq><zxx></zxx><x></x><a></a></s><mu><jqi></jqi></mu><olmwh></olmwh></bdn><yrcc></yrcc><lqzt><qup></qup></lqzt><qqc></qqc></xpv><ejg><o></o></ejg><ldm><mvhen><du></du></mvhen><l></l><tx></tx></ldm><xdyg><g><nl></nl><hwbpl></hwbpl></g<<b><h><o><ggs></ggs><unt></unt></o><vdse></vdse></h><yfqjs></yfqjs><kxcye></kxcye></b><aol></aol></xdyg><hfhrp></hfhrp></vwi><g><ovly><yudv></yudv><qe></qe></ovly><h><ayk></ayk><em></em></h><lglx></lglx></g><mk><a></a></mk><efh></efh>",
                "<i><zgpvh><u><w></w></u><rcojp><mkqg></mkqg></rcojp><y></y></zgpvh><jsbqa></jsbqa></i><vwi><xpv><bdn><lvd><u></u><rb><zza></zza></rb><brjca></brjca></lvd><s><tchq><ya></ya><lb><d></d><tkav></tkav><uxfr><g></g></uxfr><vv></vv></lb><te></te><ooq><c></c></ooq><kirpl></kirpl></tchq><zxx></zxx><x></x><a></a></s><mu><jqi></jqi></mu><olmwh></olmwh></bdn><yrcc></yrcc><lqzt><qup></qup></lqzt><qqc></qqc></xpv><ejg><o></o></ejg><ldm><mvhen><du></du></mvhen><l></l><tx></tx></ldm><xdyg><g><nl></nl><hwbpl></hwbpl></g><b><h><o><ggs></ggs><unt></unt></o><vdse></vdse></h><yfqjs></yfqjs><kxcye></kxcye></b><aol></aol></xdyg><hfhrp></hfhrp></vwi><g><ovly><yudv></yudv><qe></qe></ovly><h><ayk></ayk><em></em></h><lglx></lglx></g><mk><a></a></mk><efh></efh>"),
    ]
)
def test_correct_xml(xml_string, target_valid_xml):
    valid_xml = correct_xml(xml_string)
    print(f"valid_xml: {valid_xml}, target_valid_xml:{target_valid_xml}")
    assert valid_xml == target_valid_xml


if __name__ == "__main__":
    main()
    pytest.main(args=[__file__])
