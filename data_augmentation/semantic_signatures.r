
#setwd("C:/Users/mard019/Desktop/Documents/Conversational AI/RVI Investissement/Voice-bot/")

#source("literals.r", encoding = "utf-8")

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

Inv_account_EN <- c("TFSA"
                    , "Tax-Free Savings Account"
                    , "CELI"
                    , "RRSP"
                    , "RSP"
                    , "RESP")

Reg_account_EN <- c("chequing account"
                    , "checking account"
                    , "savings account"
)

#---# make investment #---#

make_inv_e1 <- function(action_verb = intersect(Inv_verb_EN, c("transfer", "take", "withdraw"))
                        , orig_acc = Reg_account_EN
                        , inv_acc = Inv_account_EN){
  utterances <- do.call(paste, expand.grid(action_verb
                                           , "from my"
                                           , orig_acc
                                           , c("to", "over to", "into", "to put in")
                                           , "my"
                                           , inv_acc))
  return(as.data.frame(utterances))
}


expand.grid(intersect(Inv_verb_EN, c("transfer", "take", "withdraw"))
            , "from my"
            , Reg_account_EN
            , c("to", "over to", "into", "to put in")
            , "my"
            , Inv_account_EN)

make_inv_e2 <- function(action_verb = intersect(Inv_verb_EN, c("transfer", "take", "make a transfer"))
                        , orig_acc = Reg_account_EN
                        , inv_acc = Inv_account_EN
                        , money_exp = setdiff(Money_synonyms_EN, "points")){
  utterances <- do.call(paste, expand.grid(action_verb
                                           , money_exp
                                           , "from my"
                                           , orig_acc
                                           , c("to", "over to", "into", "to put in")
                                           , "my"
                                           , inv_acc))
  return(as.data.frame(utterances))
  
}

make_inv_e3 <- function(action_verb = intersect(Inv_verb_EN, c("transfer", "take"))
                        , inv_acc = Inv_account_EN
                        , money_exp = setdiff(Money_synonyms_EN, "points")){
  utterances <- do.call(paste, expand.grid(action_verb
                                           , money_exp
                                           , c("to", "over to", "into", "to put in")
                                           , "my"
                                           , inv_acc))
  return(as.data.frame(utterances))
}

make_inv_e4 <- function(action_verb = intersect(Inv_verb_EN, c("make a contribution", "contribute", "make contribution", "make a transfer"))
                        , inv_acc = Inv_account_EN){
  utterances <- do.call(paste, expand.grid(action_verb
                                           , "to my"
                                           , inv_acc))
  return(as.data.frame(utterances))
}

make_inv_e5 <- function(action_verb = intersect(Inv_verb_EN, c("use", "trade", "convert"))
                        , inv_acc = Inv_account_EN
                        ,  money_exp = intersect(Money_synonyms_EN, "points")){
  utterances <- do.call(paste, expand.grid(action_verb
                                           , "my"
                                           , money_exp
                                           , "to add to my"
                                           , inv_acc))
  return(as.data.frame(utterances))
}

make_inv_e6 <- function(action_verb = intersect(Inv_verb_EN,c("forward", "trade", "convert"))
                        , inv_acc = Inv_account_EN
                        , money_exp = intersect(Money_synonyms_EN, "points")){
  utterances <- do.call(paste, expand.grid(action_verb
                                           , "my"
                                           , money_exp
                                           , c("towards", "for")
                                           , inv_acc))
  return(as.data.frame(utterances))
}

make_inv_e7 <- function(action_verb = intersect(Inv_verb_EN, "purchase")
                        , inv_acc = c(Inv_account_EN, "investments")){
  utterances <- do.call(paste, expand.grid(c("periodic", "recurring")
                                           , action_verb
                                           , "for my"
                                           , inv_acc))
  return(as.data.frame(utterances))
}

make_inv_e8 <- function(action_verb = intersect(Inv_verb_EN, "buy")
                        , inv_acc = c(Inv_account_EN, "investments")){
  utterances <- do.call(paste, expand.grid(action_verb
                                           , c("funds", "a GIC")
                                           , "from my"
                                           , inv_acc))
  return(as.data.frame(utterances))
}

make_inv_e9 <- function(action_verb = intersect(Inv_verb_EN, "buy")
                        , inv_acc = c(Inv_account_EN, "investments")){
  utterances <- do.call(paste, expand.grid(action_verb
                                           , c("funds", "a GIC")
                                           , "from my"
                                           , inv_acc))
  return(as.data.frame(utterances))
}

make_inv_e10 <- function(action_verb = intersect(Inv_verb_EN, "invest")
                         , inv_acc = Inv_account_EN){
  utterances <- do.call(paste, expand.grid(action_verb
                                           , "in my"
                                           , inv_acc))
  return(as.data.frame(utterances))
}


make_inv_utterances_e1 <- make_inv_e1()
make_inv_utterances_e2 <- make_inv_e2()
make_inv_utterances_e3 <- make_inv_e3()
make_inv_utterances_e4 <- make_inv_e4()
make_inv_utterances_e5 <- make_inv_e5()
make_inv_utterances_e6 <- make_inv_e6()
make_inv_utterances_e7 <- make_inv_e7()
make_inv_utterances_e8 <- make_inv_e8()
make_inv_utterances_e9 <- make_inv_e9()
make_inv_utterances_e10 <- make_inv_e10()
