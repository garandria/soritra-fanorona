import os
from pos import *

H =\
"""
\\documentclass[preview,border=4mm,convert={density=600,outext=.png}]{standalone}
\\usepackage{tikz}
\\usetikzlibrary{shapes,snakes}

% Vato
\\newcommand{\\nodec}[3]{\\node[circle,draw,minimum size=20, fill=#3] (#1#2) at (1.5*#1,1.5*#2) {};}

% Dead node -- crossed out in red
\\newcommand{\\dnode}[3]{
  \\nodec{#1}{#2}{#3};
  \\node[cross out, draw, thick, color=red] at (1.5*#1,1.5*#2) {};
}

% Trace with a label \\tracel{xy}{x'y'}{label}{left|right|above|bottom};
% \\tracel{xy}{x'y'}{}{}; without label on the arrow
\\newcommand{\\tracel}[4]{
  \\draw[->, dotted, line width=0.1cm, red] (#1)--(#2)
  node[#4, midway]{\\textbf{#3}};
}

% laka(length, height, size)
\\newcommand{\\laka}[3]{
  \\foreach \\x in {1, ..., #1}
  \\foreach \\y in {1, ..., #2}
  \\node[circle, inner sep=0pt, outer sep=0pt, fill] (\\x\\y) at (#3*\\x, #3*\\y) {};
}

\\newcommand{\\fanorontelo}{
  \\laka{3}{3}{1.5};

  \\foreach \\x [evaluate=\\x as \\sx using int(\\x+1)] in {1, 2}
  \\foreach \\y  in {1, ..., 3}
  \\draw (\\x\\y)--(\\sx\\y);

  \\foreach \\y [evaluate=\\y as \\sy using int(\\y+1)] in {1, 2}
  \\foreach \\x in {1, ..., 3}
  \\draw (\\x\\y)--(\\x\\sy);

  \\draw (11)--(22) (22)--(33);
  \\draw (13)--(22) (22)--(31);

}

\\newcommand{\\fanorondimy}{
  \\laka{5}{5}{1.5};
  
  \\foreach \\x [evaluate=\\x as \\sx using int(\\x+1)] in {1, ..., 4}
  \\foreach \\y  in {1, ..., 5}
  \\draw (\\x\\y)--(\\sx\\y);

  \\foreach \\y [evaluate=\\y as \\sy using int(\\y+1)] in {1, ..., 4}
  \\foreach \\x in {1, ..., 5}
  \\draw (\\x\\y)--(\\x\\sy);

  \\foreach \\x [evaluate=\\x as \\sx using int(\\x+1),
  evaluate=\\sx as \\ssx using int(\\sx+1)] in {1, 3}{
    \\foreach \\y [evaluate=\\y as \\sy using int(\\y+1),
    evaluate=\\sy as \\ssy using int(\\sy+1)] in {1, 3, ..., 4}{
      \\draw (\\x\\y)--(\\sx\\sy) (\\sx\\sy)--(\\ssx\\ssy);
    }
  }
  
  \\foreach \\x [evaluate=\\x as \\px using int(\\x-1),
  evaluate=\\px as \\ppx using int(\\px-1)] in {3, 5}{
    \\foreach \\y [evaluate=\\y as \\sy using int(\\y+1),
    evaluate=\\sy as \\ssy using int(\\sy+1)] in {1, 3}{
      \\draw (\\x\\y)--(\\px\\sy) (\\px\\sy)--(\\ppx\\ssy);
    }
  }
}

\\newcommand{\\fanorontsivy}{
  \\laka{9}{5}{1.5};
  
  \\foreach \\x [evaluate=\\x as \\sx using int(\\x+1)] in {1, ..., 8}
  \\foreach \\y  in {1, ..., 5}
  \\draw (\\x\\y)--(\\sx\\y);

  \\foreach \\y [evaluate=\\y as \\sy using int(\\y+1)] in {1, ..., 4}
  \\foreach \\x in {1, ..., 9}
  \\draw (\\x\\y)--(\\x\\sy);

  \\foreach \\x [evaluate=\\x as \\sx using int(\\x+1),
  evaluate=\\sx as \\ssx using int(\\sx+1)] in {1, 3, ..., 8}{
    \\foreach \\y [evaluate=\\y as \\sy using int(\\y+1),
    evaluate=\\sy as \\ssy using int(\\sy+1)] in {1, 3, ..., 4}{
      \\draw (\\x\\y)--(\\sx\\sy) (\\sx\\sy)--(\\ssx\\ssy);
    }
  }
  
  \\foreach \\x [evaluate=\\x as \\px using int(\\x-1),
  evaluate=\\px as \\ppx using int(\\px-1)] in {3, 5, ..., 9}{
    \\foreach \\y [evaluate=\\y as \\sy using int(\\y+1),
    evaluate=\\sy as \\ssy using int(\\sy+1)] in {1, 3}{
      \\draw (\\x\\y)--(\\px\\sy) (\\px\\sy)--(\\ppx\\ssy);
    }
  }  
}


\\begin{document}

\\begin{tikzpicture}
"""

T =\
"""
\\end{tikzpicture}
\\end{document}
"""

def main():
    os.system("cat pos.py | grep \"def .*()\" | tr -d ':' > fn.txt")
    fcts = []
    with open("fn.txt", 'r') as fntxt:
        for fn in fntxt:
            fcts.append(fn[4:-3])
    for fct in fcts:
        texfile = "{}.tex".format(fct)
        with open(texfile, 'w') as tex:
            tex.write(H + eval(fct + "()") + T)
        os.system("latexmk {} -shell-escape".format(texfile))
        os.system("rm {}.*".format(texfile))
    os.system("mv *.png image")
    
if __name__ == "__main__":
    main()

