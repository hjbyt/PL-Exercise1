"""
This module just contains the definitions of the terminals (tokens) and nonterminals.
"""

# EOF terminal
EOF = 'EOF'        # end of file marker

# terminals for the grammar from the recitation
LP = 'LP'          # (
RP = 'RP'          # )
ASSIGN = 'ASSIGN'  # :=
PLUS = 'PLUS'      # +
IF = 'IF'          # if
ELSE = 'ELSE'      # else
ID = 'ID'          # identifier


# nonterminals for the grammar from the recitation
P = 'P'
S = 'S'
E = 'E'
T = 'T'
EP = 'EP'


# terminals for JSON
LB = 'LB'          # {
RB = 'RB'          # }
LS = 'LS'          # [
RS = 'RS'          # ]
COMMA = 'COMMA'    # ,
COLON = 'COLON'    # :
INT = 'INT'        # an integer value
STRING = 'STRING'  # a string value


# nonterminals for JSON
obj = 'obj'
members = 'members'
keyvalue = 'keyvalue'
value = 'value'

#
# --- ADD MORE NONTERMINALS HERE IF NEEDED IN QUESTION 4
#

obj_right = 'obj_right'
members_right = 'members_right'
array = 'array'
array_right = 'array_right'
array_members = 'array_members'
array_members_right = 'array_members_right'