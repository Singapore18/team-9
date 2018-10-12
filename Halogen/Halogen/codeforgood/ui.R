#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)
library(ggplot2)
library(gridExtra)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  titlePanel("Key Performance Index"),
  
  # Sidebar with selection of x-variables 
  sidebarLayout(
    sidebarPanel(
      
      selectInput("response", "KPIs to compare:",
                         c("Growth Oriented"="g",
                           "Confident"="c",
                           "Strategic Thinking"="s",
                           "Team Player"="t",
                           "Productive"="p")),

       selectInput("variable","Variable:",
                   list("Gender"="gen",
                        "Ethnicity"="race",
                        "Household Income"="income",
                        "Workshop"="workshopid",
                        "Educational"="edu")),

      checkboxInput("outliers","Show outliers", FALSE)
                  
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      h3(textOutput("caption")),
      plotOutput("scorePlot"),
      dataTableOutput("stats")
    )
  )
))

