# Large Language Models for Optimization Modelling

Optimization is a collection of powerful mathematical techniques able to solve complex problems that possess a set of optimal solutions. It is a crucial part of business decision making, which so far has relied on human expertise to model and solve mathematical optimization problems. However, the emerging capabilities of Large Language Models (LLMs) offer significant potential in automating this process. This research explores the potential use of 4 LLMs —GPT-4, Gemini 1.5 Pro,  Claude 3 Opus, and Mixtral 8x22B— in being leveraged for a business optimization AI copilot. The research investigates how well these LLMs perform in formulating a mathematical model and solver code, from given natural language problem descriptions. Previous attempts at solving optimization problems with LLMs have yielded promising results but were mostly limited to simple optimization problems that are not representative of business applications. Hence, the dataset used in this research aims to achieve a real-world representation of business problems. It contains 16 problems spanning various optimization classes (Linear Programming (LP), Mixed-Integer Programming (MIP), Integer Programming (IP), and Nonlinear Programming (NLP)) and complexity levels. Key performance metrics include the correctness of the mathematical model, solution optimality, consistency, and code executability. The research investigates two pipelines, one with single-step prompting and one with Chain-of-Thought prompting, in order to compare the LLMs’ performance in different reasoning environments. Each problem was run 3 times, resulting in a total of 48 experiments in each pipeline.

The experiment results from four different LLMs reveal a mixed performance. GPT-4, although showed some promise, faced significant setbacks in binary variable definitions, complex constraint formulations and consistency of outputs. Mixtral 8x22B  struggled with identifying unwritten and implied model components, binary variable definitions and achieving consistent outputs as well. The optimal solution correctness of GPT-4 and Mixtral 8x22B were the lowest out of the 4 LLMs tested. Gemini 1.5 Pro was more successful, showing a higher optimality in results. However, it still struggled with the consistency of the outputs, similar to GPT-4 and Mixtral 8x22B. Furthermore, Claude 3 Opus showed the highest scores in achieving an optimal solution using the models formulated. However, it also had areas of failure, especially with constraint formulations. For all of the LLMs, there was no statistically significant evidence to suggest that the Chain-of-Thought prompting approach performed differently from the simpler, single-step prompting pipeline. Overall, these LLMs show promise in optimization modeling, however, significant gaps still remain in leveraging them for an AI Copilot application. An ensemble of these LLMs can be considered to utilize their different areas of expertise. 
 
The  project was a part of a BSc Business Analytics Thesis, hence the precise per-model analysis of the results can be found in the individual reports.
## Pipelines
<a href="url"><img src="/PipelineFlowcharts/Overview.drawio.png" align="center" width=600></a>

## Experiment outcomes


<a href="url"><img src="/Graphs_Tables/PipelinesRunsResultsChart.png" align="center"></a> 

Figure 1: A breakdown of Model and Code Solution Optimality across all individual runs. Across both pipelines only four problems were never solved correctly by any of the LLMs: IP4, MIP4, NLP3, and NLP4; only four problems were solved correctly at least once by all LLMs: IP3, LP1, and NLP1; no problem was correctly solved by all LLMs in all three runs. <br>

<a href="url"><img src="/Graphs_Tables/ModelSolutionOptimalityResultChart.png" align="center"></a>

Figure 2: The Model Solution Optimality of the four LLMs for both pipelines. For all models, Model Solution Optimality was higher in pipeline 2 than in pipeline 1. Claude 3 Opus performed best in pipeline 1, followed by Gemini 1.5 Pro, GPT-4 and finally Mixtral 8x22B. In pipelines 2, Claude 3 Opus performed best, followed by Gemini 1.5 Pro and then both GPT-4 and Mixtral 8x22B. <br>

<a href="url"><img src="/Graphs_Tables/CodeSolutionOptimalityChart.png" align="center"></a>

Figure 3: The Code Solutio Optimality of the four LLMs for both pipelines. For Claude 3 Opus, Mixtral 8x22B and GPT-4, Code Solution Optimality was higher in pipeline 2. For Gemini 1.5 Pro, Code Solution Optimality was the same in both pipelines. Claude 3 Opus and Gemini 1.5 Pro performed best in pipeline 1, followed by Mixtral 8x22B and GPT-4. In pipeline 2, Claude 3 Opus performed best, followed by Gemini 1.5 Pro, Mixtral 8x22B and GPT-4. <br>

<a href="url"><img src="/Graphs_Tables/SolutionConsinstencyChart.png" align="center"></a>

Figure 4: The Solution Consistency of the four LLMs for both pipelines. For Claude 3 Opus and Mixtral 8x22B, Solution Consistency was higher in pipeline 1, for Gemini 1.5 Pro and GPT-4 Solution Consistency was higher in pipeline 2. Gemini 1.5 Pro generated the most consistent solutions per problem in pipeline 1, followed by Claude 3 Opus, Mixtral 8x22B and GPT-4. In pipeline 2, Gemini 1.5 Pro generated the most consistent solutions per problem, followed by Claude 3 Opus, GPT-4 and Mixtral 8x22B. <br>

<a href="url"><img src="Graphs_Tables/MetricComparisonTable.png" align="center"></a>

Figure 5: A comparison of all evaluation metrics used throughout the research, except for solution consistency. Across the two pipelines, Claude 3 Opus achieved the highest score for six of the nine evaluation metrics: Model Solution Optimality (p2), Mathematical Model Correctness (p2), Parameter Correctness (p1), Objective Fnction Correctness (p1), Equivalent Code Representation of Mathematical Model (p1) and Code Solution Optimality (p2). Gemini 1.5 achieved the highest score in the other three metrics - Variable Correctness (p2), Constraint Correctness (p2) and Executability of Model-Related Code (p2) - and tied Claude 3 Opus for the highest score in Mathematical Model Correctness (p2) and Equivalent Code Representation of Mathematical Model (p2). 


## Characteristics of each problem in the dataset
<a href="url"><img src="/Graphs_Tables/ProblemCharacteristics.png" align="center"></a>
## Sources of Optimization Problems:
1.	IP_1: Wasserkrug, S., Boussioux, L., Hertog, D. D., Mirzazadeh, F., Birbil, I., Kurtz, J., & Maragno, D. (2024). From large language models and optimization to decision optimization CoPilot: A research manifesto. arXiv preprint arXiv:2402.16269.
2.	IP_2: Kurtz, J., personal communication, April 21, 2023 (data); Cornuejols, G., & Tütüncü, R. (2006). Optimization methods in finance (Vol. 5). Cambridge University Press. https://doi.org/10.1017/9781107297340 (problem logic inspiration)
3.	IP_3: Zak, E. J. (2024). How to solve real-world optimization Problems. In SpringerBriefs in operations research. https://doi.org/10.1007/978-3-031-49838-1
4.	IP_4: STEM EZ. (n.d.). Operations Research. Retrieved May 23, 2024, from https://stemez.com/subjects/science/1HOperationsReseach/1HOperationsReseach/1HOperationsResearch/1H04-0177.htm
5.	LP_1: Poler, R., Mula, J., & Díaz-Madroñero, M. (2014). Operations Research Problems Statements and Solutions (p. 16). Springer.
6.	LP_2: MOSEK ApS. (n.d.). Robust optimization. Retrieved May 23, 2024, from https://docs.mosek.com/latest/toolbox/case-studies-robust-lo.html
7.	LP_3: Poler, R., Mula, J., & Díaz-Madroñero, M. (2014). Operations Research Problems Statements and Solutions (p. 37). Springer.
8.	LP_4: Birge, J. R., & Louveaux, F. (2011). Introduction to stochastic programming. Springer Science & Business Media. https://doi.org/10.1007/978-1-4614-0237-4
9.	MIP_1 SCIP. (n.d.). Facility location problem. In SCIP Optimization Suite documentation. Retrieved May 23, 2024, from https://scipbook.readthedocs.io/en/latest/flp.html
10.	MIP_2: Poler, R., Mula, J., & Díaz-Madroñero, M. (2014). Operations Research Problems Statements and Solutions (p. 75). Springer.
11.	MIP_3: Castillo, E., Conejo, A. J., Pedregal, P., Garcia, R., & Alguacil, N. (2011). Building and solving mathematical programming models in engineering and science. John Wiley & Sons. https://doi.org/10.1007/978-3-030-97626-2
12.	MIP_4: Poler, R., Mula, J., & Díaz-Madroñero, M. (2014). Operations Research Problems Statements and Solutions (p. 146). Springer.
13.	NLP_1: Poler, R., Mula, J., & Díaz-Madroñero, M. (2014). Operations Research Problems Statements and Solutions (p. 117). Springer.
14.	NLP_2: Poler, R., Mula, J., & Díaz-Madroñero, M. (2014). Operations Research Problems Statements and Solutions (p. 97). Springer. 
15.	NLP_3: Bracken, J., & McCormick, G. P. (1968). Selected applications of nonlinear programming (pp. 28-36). Wiley. 
16.	NLP_4: Bracken, J., & McCormick, G. P. (1968). Selected applications of nonlinear programming (pp. 37-45). Wiley.

## References:
Guess what comes here

## Authors 
Annika Siefke, Hubert Perliński, Melis Doga Cevik, Nathan Ferchtandiker
