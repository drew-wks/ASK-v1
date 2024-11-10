
# Project ASK Change Log
All notable changes to this project will be documented in this file.  

## [0.5.4] - 2024-11-07
- Revisions to library admin files to make them easier to use
- Renaming prompt_ui.py to ui.py, inference.py to rag.py
- Moved balance of RAG code to rag.py so ui.py can be used with other LLMs
- Reorganized repo file directory
- Merged metadata docs and librabry list into one file called library_catalog
- Added project development workflow diagram
- Removed administration processes diagram

## [0.5.3] - 2023-12-19
### Features
- Removal of ALAUXs that announce documents in the library to avoid competing with those docs during retrieval: ALAUXs 2023 (003, 008, 012, 013, 032, 034, 036), ALAUXs 2022 (025,034, 041,042, 043)
- Developed code to delete docs from library
- Removal of Streamlit collecting summary statistics

### Bug fixes
- Removal of superceded directives: AUX-PL-007(E)
- Added missing AUX-PL-007(E)
- Number of library documents and last update date are now dynamically generated


## [0.5.2] - 2023-12-13
### Features
-Added a Spanish language example

### Bug fixes
- Added missing 2023 ALAUXes and removed outdated ones

## [0.5.1] - 2023-11-24
### Features
- Extensive readme file added to git repo

### Bug fixes
- Error message if Open AI credits are exceeded

## [0.5.0] - 2023-11-20
### Features
- Significant increase in speed (2-3x faster) 
- Additional page in library outlining product roadmap

### Bug fixes
- User warning if OpenAI service is down 
- Modifications to the prompt and hyperparameters for improved doc retrieval
- Removed two outdated policy documents

### Breaking changes
- Moved code to new github repository and relaunched user app

## [0.4.0] - 2023-11-14
### Features
- Customized the prompt to explicitly seek all requirements and to distinguish between initial and currency maintenance
- Improved naming conventions in the github repo

## [0.3.0] - 2023-11-03
### Features
- Expanded info section to provide additional informtion about the service
- Reincorporatie Truberics feedback collector
- Include search query string with results
- Ability to test without LLM call by using "pledge" as search query
- Addition of a Roadmap to git repo

### Bug fixes
- Deployed as standard form so fully accesible via mobile 

## [0.2.1] - 2023-10-26
### Features
- Add this changelog to repo. Format based on [Keep a Changelog](http://keepachangelog.com/)

### Bug fixes
- Added ASK-chat_dummy.py and a streamlit app off of it to test streamlit mobile device issues

## [0.2.0] - 2023-10-22
Lots of changes to the user interface to better explain the service and use the screen real estate  
### Features
- Added more explanatory text
- Text explaining examples disappears after first search to make more room for results  
### Bug fixes
- Eliminated formatting errors within the detailed sources  

## [0.1.1] - 2023-10-17
### Feature adds
- Reorganized repo  
- Updated logo 

### Bug fixes
- Chat window entirely inaccessible on some mobile devices.  

### Breaking changes
- Moved logo to assets directory
- Removed Truberics feedback collector for troubleshooting streamlit code

## [0.1.0] - 2023-10-14
Pushed ASK from local to public git and streamlit cloud. ASK is public!
