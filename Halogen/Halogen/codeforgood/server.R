#
# This is the server logic of a Shiny web application. You can run the 
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
library(mongolite)
library(ggplot2)

# save data and do some cleaning

# Establish connection
con= mongo(collection = "CleanedData", db = "jpcfg", url = "mongodb://randylai.2016:JpmcfgTeam9@ds129823.mlab.com:29823/jpcfg",
           verbose = FALSE, options = ssl_options())
scoredata<-con$find()
scoredata <- scoredata[,c(1:9,118:123)]
names(scoredata) <- c("userid","dob","age","gen","race","religion","income","district","edu","g","c","s","t","p","workshopid")
scoredata$race <- as.factor(scoredata$race)
scoredata$gen <- as.factor(scoredata$gen)
scoredata$income <- as.factor(scoredata$income)
scoredata$edu <- as.factor(scoredata$edu)
attach(scoredata)

# Define server logic required to draw a histogram
shinyServer(function(input, output) {
  
  ###########  THIS IS FOR MAIN DEMOGRAPHIC ##############
  score_inp <- reactive({
    score_inp <- input$response})
  var_outp <- reactive({
    var_outp <- input$variable})


  # Compute the forumla text in a reactive expression since it is 
  # shared by the output$caption and output$scorePlot expressions
  formulaText <- reactive({
      paste(input$response, "~" ,input$variable)
  })
  
  # Return the formula text for printing as a caption
  output$caption <- renderText({
    formulaText()
  })
  
  # Generate a plot of the requested variable against score and only 
  # include outliers if requested
  output$scorePlot <- renderPlot({
    
    boxplot(as.formula(formulaText()),
            data=scoredata,
            outline=input$outliers)

    })
  h4(output$stats <- renderDataTable({
    summary(input$response)
  }))

})

rm(con)
