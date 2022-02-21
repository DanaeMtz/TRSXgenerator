
#setwd("C:/Users/mard019/Desktop/Documents/Conversational AI/RVI Investissement/Voice-bot/")

#source("literals.r", encoding = "utf-8")

#---# make investment #---#

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

Inv_account_FR <- c("CELI"
                    , "compte libre d’impôt"
                    , "REER"
                    , "compte d'épargne-retraite"
                    , "REEE"
                    , "compte R trois E"
                    , "compte d’épargne pour les études")


Money_synonyms_FR <- c("de l'argent"
                       , "un montant"
                       , "une somme"
                       , "mes points"
                       , "1000 dollars"
                       , "1000 piasses"
)

Reg_account_FR <- c("compte chèques"
                    , "compte bancaire"
                    , "compte courant"
                    , "compte épargne"
)

make_inv_f1 <- function(action_verb = setdiff(Inv_verb_FR, c("ajouter", "mettre", "rajouter", "contribuer"))
                        , inv_acc = Inv_account_FR){
  utterance <- do.call(paste, expand.grid(action_verb, "dans mon", inv_acc))
  return(as.data.frame(utterance))
}


make_inv_f8 <- function(action_verb = c("programmer des virements"
                                        , "faire de l'épargne systématique"
                                        , "ajouter un prélèvement systématique")
                        , inv_acc = Inv_account_FR){
  # <verb invest> dans mon <investment account>
  utterance <- do.call(paste, expand.grid(action_verb
                                          , "dans mon"
                                          , inv_acc))
  return(as.data.frame(utterance))
}


make_inv_f3 <- function(action_verb = Inv_verb_FR
                        , money_exp = Money_synonyms_FR
                        , inv_acc = Inv_account_FR){
  #	<verb invest> <money expression> à mon <inv. account> 
  utterance <- do.call(paste, expand.grid(action_verb
                                          , money_exp
                                          , "à mon"
                                          , inv_acc))
  
  return(as.data.frame(utterance))
}


make_inv_f4 <- function(action_verb = setdiff(Inv_verb_FR, c("faire un transfert", "faire un dépôt"))
                        , money_exp = Money_synonyms_FR
                        , inv_acc = Inv_account_FR){
  # <verb invest> <money expression> dans mon <inv. account>
  utterance <- do.call(paste, expand.grid(action_verb
                                          , money_exp
                                          , "dans mon"
                                          , inv_acc))
  return(as.data.frame(utterance))
}



make_inv_f5 <- function(action_verb = intersect(Inv_verb_FR, c("faire un transfert", "faire un dépôt"))
                        , money_exp = c("d'argent" 
                                        , "de mes points"
                                        , "des fonds"
                                        , "des sous"
                                        , "de 1000 dollars"
                                        , "de 500 piasses")
                        , inv_acc = Inv_account_FR){
  # <verb invest> de <money expression> à/vers mon <inv. account>
  utterance <- do.call(paste, expand.grid(action_verb
                                          , money_exp
                                          , c("vers", "à")
                                          , "mon"
                                          , inv_acc))
  return(as.data.frame(utterance))
}






make_inv_f2 <- function(money_exp = setdiff(Money_synonyms_FR, "mes points")
                        , inv_acc = Inv_account_FR
                        , orig_acc = Reg_account_FR){
  # prendre <money expression> de mon <origin account> pour mettre dans mon/et de le mettre dans mon<inv. account>
  utterance <- do.call(paste, expand.grid("prendre"
                                          , money_exp
                                          , "de mon"
                                          , orig_acc
                                          , c("pour mettre dans", "et de le mettre dans")
                                          , "mon"
                                          , inv_acc))
  return(as.data.frame(utterance))
}




make_inv_f6 <- function(action_verb = setdiff(Inv_verb_FR, c("faire un transfert", "faire un dépôt"))
                        , money_exp = setdiff(Money_synonyms_FR, "mes points")
                        , inv_acc = Inv_account_FR
                        , orig_acc = Reg_account_FR){
  # <verb invest> <money expression> à mon <inv. account> à partir de mon <origin account>
  utterance <- do.call(paste, expand.grid(action_verb
                                          , money_exp
                                          , "à mon"
                                          , inv_acc
                                          , "à partir de mon"
                                          , orig_acc))
  return(as.data.frame(utterance))
}


make_inv_f7 <- function(action_verb = setdiff(Inv_verb_FR, c("faire un transfert", "faire un dépôt"))
                        , money_exp = setdiff(Money_synonyms_FR, "mes points")
                        , inv_acc = Inv_account_FR
                        , orig_acc = Reg_account_FR){
  # <verb invest> <money expression> de mon <origin account> à mon <investment account>
  utterance <- do.call(paste, expand.grid(action_verb
                                          , money_exp
                                          , "de mon"
                                          , orig_acc
                                          , "à mon"
                                          , inv_acc))
  return(as.data.frame(utterance))
}

make_inv_f7()

make_inv_utterances_f1 <- make_inv_f1()
make_inv_utterances_f2 <- make_inv_f2()
make_inv_utterances_f3 <- make_inv_f3()
make_inv_utterances_f4 <- make_inv_f4()
make_inv_utterances_f5 <- make_inv_f5()
make_inv_utterances_f6 <- make_inv_f6()
make_inv_utterances_f7 <- make_inv_f7()
make_inv_utterances_f8 <- make_inv_f8()
