def lakampanorontelo():
    return """
    \\fanorontelo{};
    """

def fanorontelo():
    return """
    \\fanorontelo{};

    \\nodec{1}{2}{white};
    \\nodec{1}{3}{white};
    \\nodec{2}{3}{white};
    \\nodec{3}{3}{white};
    \\nodec{1}{1}{black};
    \\nodec{2}{1}{black};
    \\nodec{3}{1}{black};
    \\nodec{3}{2}{black};
    """

def lakampanorondimy():
    return """
    \\fanorondimy{};
    """

def fanorondimy():
    return """
    \\fanorondimy{};

    % Player 1
    % --------

    \\foreach \\x in {1, ..., 5}
    \\foreach \\y in {4, 5}
    \\nodec{\\x}{\\y}{white};

    \\foreach \\x in {1, 4}
    \\nodec{\\x}{3}{white};

    % Player 2
    % -----------

    \\foreach \\x in {1, ..., 5}
    \\foreach \\y in {1, 2}
    \\nodec{\\x}{\\y}{black};

    \\foreach \\x in {2, 5}
    \\nodec{\\x}{3}{black};
    """

def lakampanorontsivy():
    return """
    \\fanorontsivy{}
    """

def fanorontsivy():
    return """
    \\fanorontsivy{}

    % Player 1
    % --------

    \\foreach \\x in {1, ..., 9}
    \\foreach \\y in {4, 5}
    \\nodec{\\x}{\\y}{white};

    \\foreach \\x in {1, 3, 6, 8}
    \\nodec{\\x}{3}{white};

    % Player 2
    % -----------

    \\foreach \\x in {1, ..., 9}
    \\foreach \\y in {1, 2}
    \\nodec{\\x}{\\y}{black};

    \\foreach \\x in {2, 4, 7, 9}
    \\nodec{\\x}{3}{black};
    """

def vaky_loha():
    return fanorontsivy() + """
    \\tracel{52}{53}{}{};
    \\dnode{5}{4}{white};
    \\dnode{5}{5}{white};
    """

def havanana():
    return fanorontsivy() +  """
    \\tracel{42}{53}{}{};
    \\dnode{6}{4}{white};
    \\dnode{7}{5}{white};
    """

def kobaka_lava():
    return fanorontsivy() +  """
    \\tracel{63}{53}{}{};
    \\dnode{7}{3}{black};
    """

def kobaka_fohy():
    return fanorontsivy() +  """
    \\tracel{63}{53}{}{};
    \\dnode{4}{3}{black};
    """

def midona():
    return lakampanorontsivy() + """
    \\nodec{3}{3}{white};
    \\dnode{6}{4}{white};
    \\dnode{6}{5}{white};
    \\nodec{6}{2}{black};
    \\nodec{8}{1}{black};
    \\tracel{62}{63}{}{};
    """

def migemo():
    return lakampanorontsivy() + """
    \\nodec{3}{3}{white};
    \\dnode{6}{4}{black};
    \\nodec{6}{3}{white};
    \\nodec{8}{1}{black};
    \\tracel{63}{62}{}{};
    """

def manenjana():
    return lakampanorontsivy() + """
    \\nodec{4}{5}{white};
    \\dnode{6}{4}{white};
    \\dnode{7}{5}{white};
    \\nodec{5}{3}{black};
    \\nodec{8}{1}{black};
    \\tracel{53}{42}{}{};
    """

def mielatra():
    return lakampanorontsivy() + """
    \\dnode{6}{3}{black};
    \\dnode{7}{3}{black};
    \\nodec{5}{3}{white};
    \\nodec{8}{1}{white};
    \\tracel{53}{43}{}{};
    """

def miriana():
    return lakampanorontsivy() + """
    \\dnode{8}{3}{black};
    \\dnode{8}{4}{black};
    \\dnode{8}{5}{black};
    \\nodec{8}{1}{white};
    \\nodec{5}{2}{black};
    \\nodec{3}{3}{white};
    \\tracel{81}{82}{}{};
    """

def mitsindrona():
    return lakampanorontsivy() + """
    \\nodec{4}{2}{black};
    \\nodec{8}{1}{black};
    \\nodec{2}{3}{white};
    \\dnode{6}{4}{white};
    \\dnode{7}{5}{white};
    \\tracel{42}{53}{}{};
    """

def miforitra():
    return lakampanorontsivy() + """
    \\nodec{8}{4}{black};
    \\nodec{1}{1}{black};
    \\nodec{2}{3}{white};
    \\dnode{7}{3}{white};
    \\dnode{9}{3}{white};
    \\tracel{84}{75}{1}{right};
    \\tracel{75}{74}{2}{left};
    """

def mihazakazaka():
    return lakampanorontsivy() + """
    \\nodec{2}{1}{black};
    \\nodec{8}{1}{black};
    \\dnode{2}{3}{white};
    \\dnode{4}{4}{white};
    \\tracel{21}{22}{1}{right};
    \\tracel{22}{33}{2}{right};
    """

def mikileva():
    return lakampanorontsivy() + """
    \\nodec{3}{2}{black};
    \\nodec{8}{1}{black};
    \\dnode{3}{4}{white};
    \\dnode{4}{3}{white};
    \\dnode{5}{5}{white};
    \\tracel{32}{33}{1}{left};
    \\tracel{33}{44}{2}{right};
    \\tracel{44}{45}{3}{right};
    """

def mivadika():
    return lakampanorontsivy() + """
    \\nodec{3}{1}{white};
    \\nodec{8}{4}{black};
    \\dnode{5}{3}{white};
    \\dnode{9}{3}{white};
    \\tracel{84}{75}{1}{right};
    \\tracel{75}{64}{2}{left};
    """

def mikizo():
    return lakampanorontsivy() + """
    \\nodec{9}{5}{black};
    \\nodec{9}{4}{black};
    \\nodec{8}{4}{black};
    \\dnode{9}{3}{white};
    \\nodec{9}{2}{white};
    \\tracel{84}{75}{}{};
    """

def mamoina():
    return lakampanorontsivy() + """
    \\nodec{1}{2}{white};
    \\nodec{2}{1}{white};
    \\nodec{3}{3}{black};
    """

def miampify():
    return lakampanorontsivy() + """
    \\nodec{8}{1}{white};
    \\nodec{8}{2}{white};
    \\nodec{9}{1}{white};
    \\nodec{8}{3}{black};
    """

def mihemotra():
    return lakampanorontsivy() + """
    \\nodec{2}{1}{white};
    \\nodec{2}{2}{white};
    \\nodec{5}{2}{black};
    \\nodec{3}{4}{black};
    \\tracel{52}{53}{}{};
    """

def mandroso():
    return lakampanorontsivy() + """
    \\nodec{1}{2}{white};
    \\nodec{4}{1}{white};
    \\nodec{9}{1}{white};
    \\nodec{1}{5}{black};
    \\nodec{3}{3}{black};
    \\nodec{4}{4}{black};
    \\tracel{33}{22}{}{};
    """
