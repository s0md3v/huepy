#!/usr/bin/python3

from huepy import *

def Preview():
    print("")
    print(bold("    AVAILABLE COLORS    ")+bold("    AVAILABLE STYLES    ")+bold("    AVAILABLE MODES"))
    print("")
    print(white("  ████████████████████  ")+bold("       Bold Text             ")+info(under("Info")+ " Sign!"))
    print(grey("  ████████████████████  ")+"       "+bg("BackGround")+"            "+que(under("Que")+ " Sign!"))
    print(black("  ████████████████████  ")+"       "+under("Under Line")+"            "+run(under("Run")+ " Sign!"))
    print(green("  ████████████████████  ")+"     "+strike("Strike Through")+"          "+bad(under("Bad")+ " Sign!"))
    print(lightgreen("  ████████████████████  ")+italic("      Italic Text            ")+good(under("Good")+ " Sign!"))
    print(cyan("  ████████████████████       ")+bold(under("Bold Underline")))
    #print(lightcyan("  ████████████████████        ")+bold(strike("Bold Strike")))
    print(red("  ████████████████████        ")+bold(italic("Bold Italic")))
    print(blue("  ████████████████████"))
    print(lightblue("  ████████████████████"))
    print(purple("  ████████████████████"))
    print(lightpurple("  ████████████████████"))
    print(orange("  ████████████████████"))
    print(yellow("  ████████████████████"))


def Help():
    Preview()
    print("""
    Colors :  white, grey, black, green, lightgreen, lgreen, cyan, lightcyan, lcyan
              red, blue, lightblue, lblue, purple, lightpurple, lpurple, orange, yellow

        print(red("This is Red Colored Text"))

        print(lightcyan("This is Red Colored Text"))
                        or
        print(lcyan("This is Red Colored Text"))

    Styles :  bold, bg, under, strike, italic

        print(bold("Some Text"))
        print(bold(italic("Some more Text")))

    Modes  :  info, que, run, bad, good

        print(bad("An error occured!"))
    """)


if __name__ == "__main__":
    Help()
