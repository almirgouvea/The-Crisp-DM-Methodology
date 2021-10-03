#!/usr/bin/env python
# coding: utf-8

# <center>
# 
# # The CRISP-DM Model
#     
# </center>

# ## Definition

# The CRoss-Industry Standard Process for Data Mining (CRISP-DM), created in the end of 1996 by leaders of Daimler-Benz, is a non-proprietary, documented and freely available data mining methodology and process model.

# This model encourages best practices and offers organizations the structure needed to realize better, faster results from data mining due the complete blueprint for conducting a data mining project.

# After many changes on CRISP-DM, a significant progress occurs on 2000 due a development of a standardized data processing model accepted by industry players.

# CRISP-DM provides a generic process model capable of being modified for the particular needs of any industry.

# The data mining methodology and techniques combined with assistance from more experienced practitioners can be an essential tool to understand the concepts and steps involved in the entire data mining process.

# CRISP-DM organizes the data mining process into six phases: business understanding, data understanding, data preparation, modeling, evaluation, and deployment.

# The arrows indicates the dependencies between the phases and the outer circle symbolizes the cyclical nature of data mining itself.

# After complete the cyciclal the lessons learned can be analysed and show to business team. After it can be more focus on business questions and start again focusing on get other analysis.

# <div>
# 
# <img src="attachment:Crispdm.png" width = "700"/>
#     
# </div>

#                                         Figure 01: Phases of the CRISP-DM

# ## Phase one: Business Understanding

# This phase aims to understand the project objectives and requirements from a business perspective, converting the knowledge into a data mining problem definition and then developing a preliminary plan to achieve the objectives.

# Understanding what the customer really wants to accomplish from a business perspective is very important to find a solution to the problem.

# There are several keys steps to develop the business understanding process:
# 
# - determining business objectives
# - assessing the situation
# - determine the data mining goals
# - producing the project plan

# ### Determining business objectives

# Understanding a client's true goal is critical:
# - to uncover the primary business objective
# - to uncover the related questions the business would like to address
# - to uncover important factors involved in the planned project
# - to ensure the projects answers correctly the expected business questions
# - to measure the success to make sure that each success criterion relates to at least one of the specified business objectives

# ### Assess the situation

# This task involves the resources, requirements, constraints, assumptions, risks, contingencies, glossary of terminology, and the cost-benefit analysis.

# This step is very important to outline the resources available to accomplish the data mining project to:
# - list personnel resources like business experts, data experts, technical support, and data mining experts
# - discover what data is available to meet the primary business goal
# - list of computing resources focusing on hardware platforms
# - list software resources like data mining tools, other relevant software

# It is important to describe the requirements, assumptions, and constraints to:
# - schedule of completion, comprehensibility, and quality of results, and security, as well as legal issues
# - list the assumptions made in the project and the unverifiable assumptions about the business questions
# - list the project risks when considering the assumptions
# - list of constraints on the project considering resources availability and technological constraints 

# It is important to insvestigate the risks and contingencies to:
# - list the risks or events that might delay the project or cause it to fail
# - list contingency plans to determine what actions should be taken if risks or events occur
# - list the potential solution of the risks

# It is important to compile a glossary of terminology relevant to the project including two components:
# - a glossary of relevant business terminology to help other teams understand the business issue related to the project
# - a glossary of data mining terminology illustrated with examples

# It is important to verify the costs and benefits due project's implementation including:
# - construct a cost-benefit analysis for the project comparing the project costs with the potential benefits
# - compare the cost-effectiveness as specifically as possible

# ### Determine the data mining goals

# The goals of data mining are to transform the business problem into a technical problem to apply the concepts of the crisp-dm methodology.

# To achieve the business objective it is important to describe:
# - the intended outputs of the project
# - the criteria for a successful outcome project

# It is important to analyze whether:
# - the business success criteria were defined subjectively and by whom
# - defines the objective effectively, otherwise, it will be necessary to re-examine the problem definition

# ### Producing the project plan

# This step describes the intended plan for achieving the data mining goals including:
# - outline the specific steps to be performed during the project
# - proposed timeline on each stage of the project
# - duration, resources required, inputs, outputs, and dependencies of the project stages
# - an analysis of dependencies between schedule and risks
# - an assessment of potential risks, considering the actions and recommendations to be taken
# - an initial assessment of the tools and techniques needed to support the project

# The proposed timeline depends on each project phase, so it is important to decide which evaluation strategy will be used in the stages.

# The industry timeline standards are:
# - Data Preparation: 50 to 70 percent
# - Data Understanding: 20 to 30 percent
# - Modeling, Evaluation, and Business Understanding: 10 to 20 percent
# - Deployment Planning: 5 to 10 percent

# <div>
#     
# <img src = "attachment:Industry_timeline_standards.svg" width = '800'/>
# 
# </div>

#                         Figure 02: Generally accepted industry timeline standards

# ## Phase Two: Data Understanding

# This phase aims to increase familiarity with the data, to identify data quality problems, to discover initial insights into the data and detect interesting subsets to form hypotesis about hidden information.

# There are several keys steps to develop the data understanding process:
# - collection of initial data
# - description of the data
# - exploration the data
# - verification data quality

# ### Collect the Initial data

# This step consists on acquires the necessary data from several sources.

# Understanding the process to collect data is critical:
# - to determine how to loading and integrating the data in the process
# - the datasets acquired, the location where they are stored, and the methods used to acquire them
# - to analyze the potential delay to collect data from each source due to long lag time
# - to report problems encountered and propose solutions to avoid it

# ### Describe the data

# This step is very important to understand the data by checking the properties of the acquired data, such as:
# - the format of the data
# - the quantity of the data, for example, the number of records and fields in each table
# - the identities of the fields
# - the features of the data

# ### Explore the Data

# Exploring the data help tackles the data mining questions considering assumptions and potential impact on the remainder of the project.

# This task also refines the data description by performing the transformation and other data preparation steps necessary for further analysis.

# This process can be done using:
# - querying, visualization and reporting techniques
# - an analyzis of key attributes relationships between pairs or small numbers of attributes
# - statistical analyzes including graphs and plots
# - analyzing the initial hypothesis and its impact on the rest of the project

# ### Verify Data Quality

# Data quality is essential to ensure project success.

# After analyzing the data to verify data quality, it is important to answer some questions such as:
# - Is there missing attributes and blank fields?
# - Does it cover all the cases required?
# - Are the collected values possible to occur or are they outliers?
# - How often do errors and missing values in the data occur?
# - Are there attributes with different values that have similar meanings?
# - Does the acquired data satisfy the relevant requirements?
# - Does it necessary to a collect different sets of data?

# It is important to provide a data quality report containing:
# - list the results of the data quality verification
# - consider both data and business knowledge to solve data quality issues
# - list possible solutions when occurs quality problem

# <div>
#     
# <img src="attachment:sources_data.png" width="700">
#     
# </div>

#                                 Figure 03: Different sources of the data                          

# ## Phase Three: Data Preparation

# This phase aims to build the final dataset to be used in the modeling tools.

# There are several keys steps to develop the data preparation process:
# - data selection
# - data cleaning
# - data construction
# - data integration
# - data formatting

# ### Select Data

# Several criteria must be considered when deciding which of the data will be used in the analysis:
# - its relevance to achieving data mining objectives
# - the quality and technical constraints such as limits on data volume or data types
# - choose and explain which certain data must be included or excluded
# - which attributes (columns) are more important than others
# - which records (rows) are more important than others

# ### Clean Data

# Data cleaning is an important process to ensure quality, representativeness, and unbiased.

# The data cleaning process considers the following steps:
# - selection of clean subsets of the data
# - the insertion of suitable defaults
# - estimation of missing data by modeling 

# It is important to provide a clean data report containing:
# - decisions and actions that were taken to resolve data quality issues
# - the data transformations that took place in this step
# - possible impact on the result of the project analysis

# ### Construct Data

# Construct data is the process of developing new records or producing derived attributes.
# 
# - New records focus on creating a new attribute column from a data collect.
# 
# - Derived attributes focus on constructing new of it from one or more existing attributes in the same record.
# 
# It is important to consider adding derived attributes only to facilitate the modeling process or the modeling algorithm, not to reduce the number of input attributes.

# ### Integrate Data

# Integrate data focus on combining information from multiple tables or records to create new records or value.

# The integrate data process can be done by different ways such as:
# 
# - two or more tables with different information about the same object can be merged together to create a new table with fields from the source tables
# - perform the aggregation operation in which new values are created from summarizing information from various records and/or tables.

# ### Format Data

# The data formatting process primarily focuses on syntactic modifications made to the data without changing its meaning.
# 
# Sometimes is necessary to change the design or format of the data, or change the order of the attributes to make it suitable for a specific modeling tool, or answer the data mining question.

# <div>
#     
# <img src = "attachment:data_preparation.png" width = '700'/>
# 
# </div>

#                       Figure 04: Need to care in the process of the data preparation                     

# ## Phase Four: Modeling

# This phase aims to select and apply modeling techniques to calibrate their parameters to optimal values.

# There are several keys steps to develop the modeling process:
# - selection of the modeling technique
# - generation of test design
# - creation of models
# - assessment of models

# ### Select the Modeling Technique

# The selection of the modeling technique focuses on choosing one or more modeling techniques and the assumptions associated to the modeling technique.

# When perform the select the modeling technique process it is important to:
# - document the actual modeling technique that is to be used
# - If multiple techniques are applied, perform this task separately for each one
# - record any assumption made about the data

# ### Generate Test Design

# To determine the strength, quality, and validity of the model, before building the model, is necessary running empirical testing to measure how well the model can predict history before using it to predict the future.

# There are several keys steps to develop the test design:
# - describe the process for training, testing, and evaluating the model
# - separate dataset into train and test
# - build the model in the train set
# - estimate the quality in the test set

# ### Build the Model

# This task focus on run the modeling tool on the prepared data set to create one or more models.

# There are several keys steps to develop the build model process:
# - list the model parameters and their chosen values
# - provide a rationale for choosing parameter settings
# - describe the resulting models
# - describe how to interpret the models and their peculiarities

# ### Assess the Model

# Assess the model has focused on interprets the model based on domain knowledge of the subject analyzed, project success criteria, desired test design, and the data mining results in the business context.

# There are several keys steps to develop the model assessment process:
# - apply a single technique more than once or generates data mining results with several different techniques
# - compare all results according to the evaluation criteria
# - summarize results of this task
# - list qualities of generated models
# - rank models quality by comparing them with each other
# - revise parameters settings, tune them and build a new model with it
# - iterate model building and assessment until found the best model considering the criteria
# - document all revisions and assessments

# <div>
#     
# <img src= "attachment:modeling_techniques.png" width= '700'/>
#     
# </div>

#                                   Figure 05: Modeling technique process

# ## Phase Five: Evaluation

# This phase aims to evaluate the model and review the model construction steps to ensure it adequately achieves business objectives and also to verify if considered all business issues.

# There are several keys steps to develop the evaluation proccess:
# - evaluation of results
# - process review
# - determination of next steps

# ### Evaluation of results

# Evaluation of results focuses on assessing how well the model meets business objectives:
# - checking situations where the model is not efficient
# - testing the models on real-world applications
# - seeking for additional challenges, information or hints

# At the end of this step is very important to summarize the assessment results in terms of business success criteria analyzing if the project already meets the initial business objectives.

# ### Process review

# Process review focuses on quality assurance through analyzing all steps to guarantee the project covers all proposed business issues.

# It is important to summarize this task by highlighting missed activities and those that must be repeated.

# ### Determination of next steps

# Determining the next steps focuses on project leader analysis to decide what should be done next:
# - finish the project and start the deployment
# - initiate further iterations
# - set up new projects

# At the end of this step is very important:
# - to analyze of remaining resources and budget
# - list the potential further actions with pros and cons for each
# - describe the decision, the justification, and how to proceed with it

# <div>
# 
# <img src= "attachment:business_team.png" width = '700' />
# 
# </div>

#                       Figure 06: Evaluation the results and determine next steps           

# ## Phase Six: Deployment

# This phase aims to organize and present the knowledge acquired with the project so that the client can use the created models in the organization's decision-making processes.

# There are several keys steps to develop the deployment proccess:
# - plan deployment
# - plan monitoring and maintenance
# - the production of the final report
# - review of the project

# ### Plan deployment

# This task considers the analyzes of the results of the model assessment to plan deployment development strategies.

# It is important to summarize the deployment strategy, the steps required to carry it out, and how to perform it.

# ### Plan monitoring and maintenance

# To avoid misuse of data mining results in the business environment, it is vital to plan monitoring and maintenance strategies.

# It is important to summarize the plan monitoring and maintenance strategies, the steps required to carry it out, and how to perform it.

# ### Production of the final report

# The production of the final report must be written by the project leader team considering all previous deliverables, summarizing and organizing the results.

# Deployment plan decides which is the type of the final report:
# - a summary of the project and its experiences
# - a final and comprehensive presentation of the data mining results
# - a meeting at the end of the project to present the results to the customer

# ### Review of the project

# Review of the project focuses on include a summary of important experiences during the project:
# - failures
# - success
# - potential areas of improvement for use in future projects
# - interviews with the significant project participants
# - pitfalls
# - misleading approaches
# - hints for selecting the most suitable data mining techniques for similar situations
# - individual project member reports written during project phases and tasks

# <div>
#     
# <img src = "attachment:deployment.png" width = "700" >
# 
# </div>

#                       Figure 07: Monitoring, maintenance, and project deployment                      

# All of the above steps are summarized in the outline of the phases, containing the generic tasks (bold) and outputs (italics).

# <div>
# 
# <img src= "attachment:generic_steps_crispdm.png" width='900'>
#     
# </div>

#                 Figure 8: Generic tasks (bold) and outputs (italic) of the CRISP-DM reference model.

# ## References

# - The Journal of Data Warehousing [The New Blueprint for Data Mining](https://mineracaodedados.files.wordpress.com/2012/04/the-crisp-dm-model-the-new-blueprint-for-data-mining-shearer-colin.pdf)
# 
# 
# - Free images obtained from the following sites: [UNSPLASH](https://unsplash.com/), [PIXABAY](https://pixabay.com/) and [FREEPIK](https://image.freepik.com)
