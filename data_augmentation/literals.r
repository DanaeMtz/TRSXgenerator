
library("tidyverse")

#---# ACCOUNT TYPES #---#

registered_plans_FR <- c("CELI" = "CELI"
                         , "CELI" = "Compte d’épargne libre d’impôt"
                         , "CELI" = "Compte libre d’impôt"
                         , "REER" = "REER"
                         , "REER" = "Régime enregistré d’épargne retraite"
                         , "REER" = "Compte d'épargne-retraite" 
                         , "REEE" = "REEE"
                         , "REEE" = "Régime enregistré d’épargne-études"
                         , "REEE" = "Régime d'épargne de mes enfants"
                         , "REEE" = "Compte d’épargne pour les études"
                         , "REEE" = "Compte R trois E"
                         , "CPG"  = "CPG" # not a plan, but can be placed in a CELI or in a REER 
                         , "CPG"  = "Certificat de placement garanti"
                         , "CPG"  = "Certificat"
                         , "CPG"  = "Placement garanti"
)

registered_plans_EN <- c("TFSA" = "TFSA"
                         , "TFSA" = "Tax-Free Savings Account"
                         , "TFSA" = "CELI"
                         , "RRSP" = "RRSP"
                         , "RRSP" = "Registered Retirement Savings Plan"
                         , "RRSP" = "Retirement Savings Plan" 
                         , "RRSP" = "RSP" # client autilise aussi le terme "RSP" pour RRSP
                         , "RESP" = "RESP"
                         , "RESP" = "Registered Education Savings Plan"
                         , "GIC" = "GIC" # not a plan, but can be placed in a TFSA or in a RRSP 
                         , "GIC" = "Guaranteed Investment Certificate"
)

# investment accounts #
Inv_account_FR <- c("CELI"
                    , "compte libre d’impôt"
                    , "REER"
                    , "compte d'épargne-retraite"
                    , "REEE"
                    , "compte R trois E"
                    , "compte d’épargne pour les études")

Inv_account_EN <- c("TFSA"
                    , "Tax-Free Savings Account"
                    , "CELI"
                    , "RRSP"
                    , "RSP"
                    , "RESP")

# remark: GICs can be placed in an RRSP or TFSA or held in an unregistered account (without a plan)

Annuities_retirement_funds_FR <- c("FERR" = "FERR"
                                   , "FERR" = "Fonds enregistré de revenu de retraite"
                                   , "FERR" = "Compte de revenu de retraite"
                                   , "CRI" = "CRI"
                                   , "CRI" = "Compte de retraite immobilisé"
                                   , "FRV" = "FRV"
                                   , "FRV" = "Fonds de revenu viager"
)

Annuities_retirement_funds_EN <- c("RRIF" = "RRIF"
                                   , "RRIF" = "Registered Retirement Income Funds"
                                   , "LIRA" = "LIRA"
                                   , "LIRA" = "Locked-in Retirement Accounts"
                                   , "LIF" = "LIF"
                                   , "LIF" = "Life Income Funds"
)
# Remark: clients won't say "open a FERR/RRIF, FRV/LIF" so these types of account are only to be considered in the amendment requests.

regular_accounts_FR <- c("Compte chèques" = "Compte chèques"
                         , "Compte chèques" = "Compte bancaire" 
                         , "Compte chèques" = "Compte courant"  
                         , "Compte épargne à intérêt élevé" = "Compte épargne à intérêt élevé"
                         , "Compte épargne à intérêt élevé" = "Compte épargne"
                         , "Compte épargne à intérêt élevé" = "Compte d'épargne"
)

regular_accounts_EN <- c("Chequing account" = "Chequing account"
                         , "Chequing account" = "Checking account"
                         , "HISA" = "HISA"
                         , "HISA" = "High Interest Savings Account"
                         , "HISA" = "Savings account"
)

# regular accounts #

Reg_account_FR <- c("compte chèques"
                    , "compte bancaire"
                    , "compte courant"
                    , "compte épargne"
)

Reg_account_EN <- c("chequing account"
                    , "checking account"
                    , "savings account"
)

#for(plan in registered_plans_FR){print(plan)}
#for(plan in registered_plans_EN){print(plan)}
#for(account in regular_accounts_FR){print(account)}
#for(account in regular_accounts_EN){print(account)}

# Invest VERBS #

Inv_verb_EN <- c("buy"
                 , "contribute"
                 , "convert"
                 , "forward"
                 , "invest"
                 , "make a contribution"
                 , "make a transfer"
                 , "make contribution"
                 , "purchase"
                 , "take"                
                 , "trade"               
                 , "transfer"            
                 , "use"                 
                 , "withdraw"
) 

Inv_verb_FR <- c("ajouter"            
                 , "contribuer"         
                 , "cotiser"            
                 , "déposer"            
                 , "épargner"           
                 , "faire un dépôt"     
                 , "faire un transfert" 
                 , "investir"           
                 , "mettre"             
                 , "placer"            
                 , "rajouter"           
                 , "transférer"
)


# Money synonyms 

Money_synonyms_FR <- c("de l'argent"
                       , "un montant"
                       , "une somme"
                       , "mes points"
                       , "1000 dollars"
                       , "1000 piasses"
)

Money_synonyms_EN <- c("money"
                       , "some money"
                       , "funds"
                       , "the funds"
                       , "points"
                       , "1000 dollars"
)


#action_verb_wit_1 <- c("retirer", "sortir", "déplacer", "prendre", "faire transférer", "transférer", "enlever")
#
#money_exp_1 <- c("de l'argent", "un montant", "une somme", "mes points", paste(seq(100, 1500, by = 200), "dollars"))
#
#money_exp_2 <- c("d'argent" 
#                 , "de mes points"
#                 , "des fonds"
#                 , "des sous"
#                 , "de 1000 dollars"
#                 , "de 1000 piasses")
#
#orig_account <- c("compte-chèques", "compte chèque", "compte de banque", "compte bancaire", "compte épargne")
#adj_poss     <- c("mon", "mon compte")