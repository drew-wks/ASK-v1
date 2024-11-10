#### ASK Feature Roadmap
**Note: This is a working legacy branch of ASK and no longer under development. The roadmap only relates to items to ensure this repo is usable by others, bug fixes, and that the records created by it in the vector db have ids created based on UUIDv5 standard and thus can serve as unique identifiers across databases. All future development will occur on another branch.**

##### Library Management: the documents ASK uses to provide responses
[x] 01NOV2024 Updated pre-processing script to calculate UUIDv5 off of entire PDF rather than first two pages
[x] Compelted the find and delete vectors notebook and provided good doucmentation
[x] Enable direct export of Library List Report from Qdrant into UI via xlsx  
[x] Check duplicate PDFs feature directly at the vector db "source of truth" 
[x] Review, modify, delete documents directly at the vector db  
[x] Remove PDFs - achieved via langchain.vectorstores.qdrant.Qdrant.delete([vector IDs])  
[x] Evaluate Ray for ASK  

##### Speed and Accuracy: continue to improve the results
[x] Explore better prompts through prompt templates  
[x] Tune retrieval hyperparameters such as lambda, k-means 
[x] Tag documents with effective date  
[x] Get Streamlit working faster via st.session_state and st.cache_resource  
[x] Insert a pre-prompting/inference step to ensure all relevant dos are retrieved
[ ] Reason through contradictions in corpus docs (e.g., conflicting policies)
[ ] Index additional metadata  
[ ] Include effective date in retrieval   
[ ] Give greater to weight to more recent documents: currently assessing   
[ ] Explore other chunking strategies: may not be necessary  
[ ] Test other private and [open-source embedding models](https://huggingface.co/spaces/mteb/leaderboard) incl. cohere, anarchy  

##### UI Enhancements: making ASK easier to use  
[x] Implement workaround chat input field on mobile devices (a bug with streamlit)  
[x] Bring feedback back into the UI  
[x] Incorporate better visual status into UI  
[x] Add a warning when the underlying LLM (e.g., OpenAI) is down  

##### Instrumentation: tooling to measure and assess performance  
[x] Assess instrumentation providers: wandb, neptune, Trubrics  
[ ] Continue to build out on Trubrics  
[ ] Add tokens usage to truberics  
[ ] Add parameters to trubrics feed  
[ ] Explore IP address gathering on Streamlit cloud  
[ ] Explore Neptune platform  

##### Administration: simplify backend through automation  
[x] Evaluate Vectara db  
[ ] Utilize agents to replace programmatic work such as bringing metadata into chunks  
[ ] Explore having agent extract doc purpose and incorporate as metadata  
