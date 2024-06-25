# Large Language Models for Optimization Modelling

General information on the experiment 

## Pipelines
<a href="url"><img src="/PipelineFlowcharts/Overview.drawio.png" align="center" width=600></a>

## Experiment outcomes
Here put graphs and all

<figure style="text-align: center;">
    <a href="url">
        <img src="/Graphs_Tables/PipelinesRunsResultsChart.png" alt="Pipeline Runs Results">
    </a>
    <figcaption>Figure 1: Pipeline Runs Results </figcaption>
</figure>
Figure 1 shows a breakdown of Model and Code Solution Optimality across all individual runs. Across both pipelines only four problems were never solved correctly by any of the LLMs: IP4, MIP4, NLP3, and NLP4; only four problems were solved correctly at least once by all LLMs: IP3, LP1, and NLP1; no problem was correctly solved by all LLMs in all three runs.

<figure style="text-align: center;">
    <a href="url">
        <img src="/Graphs_Tables/ModelSolutionOptimalityResultChart.png" alt="Model Solution Optimality">
    </a>
    <figcaption>Figure 2: Model Solution Optimality </figcaption>
</figure>
Figure 2 shows the Model Solution Optimality of the four LLMs for both pipelines. For all models, Model Solution Optimality was higher in pipeline 2 than in pipeline 1. Claude 3 Opus performed best in pipeline 1, followed by Gemini 1.5 Pro, GPT-4 and finally Mixtral 8x22B. In pipelines 2, Claude 3 Opus performed best, followed by Gemini 1.5 Pro and then both GPT-4 and Mixtral 8x22B.

<figure style="text-align: center;">
    <a href="url">
        <img src="/Graphs_Tables/CodeSolutionOptimalityChart.png" alt="Code Solution Optimality">
    </a>
    <figcaption>Figure 3: Code Solution Optimality </figcaption>
</figure>
Figure 3 shows the Code Solutio Optimality of the four LLMs for both pipelines. For Claude 3 Opus, Mixtral 8x22B and GPT-4, Code Solution Optimality was higher in pipeline 2. For Gemini 1.5 Pro, Code Solution Optimality was the same in both pipelines. Claude 3 Opus and Gemini 1.5 Pro performed best in pipeline 1, followed by Mixtral 8x22B and GPT-4. In pipeline 2, Claude 3 Opus performed best, followed by Gemini 1.5 Pro, Mixtral 8x22B and GPT-4.

<figure style="text-align: center;">
    <a href="url">
        <img src="/Graphs_Tables/SolutionConsinstencyChart.png" alt="Solution Consistency">
    </a>
    <figcaption>Figure 4: Solution Consistency </figcaption>
</figure>
Figure 4 shows the Solution Consistency of the four LLMs for both pipelines. For Claude 3 Opus and Mixtral 8x22B, Solution Consistency was higher in pipeline 1, for Gemini 1.5 Pro and GPT-4 Solution Consistency was higher in pipeline 2. Gemini 1.5 Pro generated the most consistent solutions per problem in pipeline 1, followed by Claude 3 Opus, Mixtral 8x22B and GPT-4. In pipeline 2, Gemini 1.5 Pro generated the most consistent solutions per problem, followed by Claude 3 Opus, GPT-4 and Mixtral 8x22B.

<figure style="text-align: center;">
    <a href="url">
        <img src="Graphs_Tables/MetricComparisonTable.png" alt="Metrics Comparison">
    </a>
    <figcaption>Figure 5: Metrics Comparison </figcaption>
</figure>
Figure 5 shows a comparison of all evaluation metrics used throughout the research, except for solution consistency. Across the two pipelines, Claude 3 Opus achieved the highest score for six of the nine evaluation metrics: Model Solution Optimality (p2), Mathematical Model Correctness (p2), Parameter Correctness (p1), Objective Fnction Correctness (p1), Equivalent Code Representation of Mathematical Model (p1) and Code Solution Optimality (p2). Gemini 1.5 achieved the highest score in the other three metrics - Variable Correctness (p2), Constraint Correctness (p2) and Executability of Model-Related Code (p2) - and tied Claude 3 Opus for the highest score in Mathematical Model Correctness (p2) and Equivalent Code Representation of Mathematical Model (p2). 


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
