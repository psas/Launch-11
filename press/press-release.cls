%----------------------------------------------------------------------------%
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{press-release}[2014/07/20 PSAS Press Release]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{letter}}
\ProcessOptions\relax
\LoadClass[12pt]{article}

%----------------------------------------------------------------------------%

\RequirePackage[paperwidth=8.5in,paperheight=11in,inner=0.5in,outer=0.5in,top=0.5in,bottom=0.5in]{geometry}
\RequirePackage{xcolor}
\RequirePackage{titlesec}
\RequirePackage{fancyhdr}
\RequirePackage{ragged2e}
\RequirePackage{graphicx}
\RequirePackage{wrapfig}

% Custom colours
\definecolor{psugreen}{rgb}{0.41568627451,0.498039215686,0.0627450980392}
\definecolor{dark-gray}{gray}{0.3}

\renewcommand{\familydefault}{\sfdefault}
\renewcommand{\maketitle}{}

% Pagesize, we want tight margins and a header that sticks very near the top
\addtolength{\voffset}{-0.75in}
\setlength{\topmargin}{0.0in}
\setlength{\headheight}{0.75in}
\setlength{\headsep}{0.2in}
\setlength{\textheight}{8.5in} 
\setlength{\footskip}{0.6in}

% fancy package for easy headers and footers
\pagestyle{fancy}
\fancyhead{}
\fancyfoot{}

% Remove header and footer line
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Header has our letterhead graphic in it
\fancyhead[LO,LE]{%
\includegraphics[]{images/header}%
}

% Footer is just the page number
\fancyfoot[LO,LE]{%
\thepage
}

% Setting the size of the section and subsection commands
\titleformat{\section}
  {\normalfont\sffamily\LARGE\bfseries\color{psugreen}}
  {\thesection}{1.0em}{}

\titleformat{\subsection}
  {\normalfont\sffamily\normalsize\bfseries\color{psugreen}}
  {\thesection}{0em}{}

% Take the slack out of the subsection text, no space after it
\titlespacing\subsection{0pt}{1.0em}{0.33em}


% General document style
\color{dark-gray}
\setlength\parindent{0pt}
\setlength{\parskip}{1.2em}
\linespread{0.9}
\RaggedRight

