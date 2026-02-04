# python-libraries-for-ds
Curated list of python libraries for data, science, and data science. 

# Data Science Libraries


## Personal Favorites

- Polars
- Plotly
- GreatTables
- Quarto
- uv
- warp


## Editors

### Notebook Environments
- **[Jupyter Notebook](https://github.com/jupyter/notebook)** (12.9k GitHub stars): Classic notebook interface. Cell-based execution, markdown support, inline plots. Most popular Python notebook.
- **[JupyterLab](https://github.com/jupyterlab/jupyterlab)** (15.1k GitHub stars): Next-generation web-based interface for Jupyter. More features than classic Jupyter, extensible. Built on Jupyter.
- **[marimo](https://github.com/marimo-team/marimo)** (18.8k GitHub stars): Reactive Python notebook. Cells automatically update when dependencies change. No hidden state, reproducible. Modern alternative to Jupyter.
- **[IPython](https://github.com/ipython/ipython)** (16.7k GitHub stars): Enhanced interactive Python shell. Tab completion, magic commands, rich display. Powers Jupyter notebooks.
- **Google Colab**: Free cloud-based Jupyter notebook environment. GPU/TPU access, collaborative editing. No installation needed.
- **Kaggle Notebooks**: Cloud-based notebook environment. Integrated with Kaggle datasets and competitions. Free GPU access.

### IDE-Based Interactive Environments
- **[VS Code with Python](https://github.com/microsoft/vscode)** (181.2k GitHub stars): VS Code with Python extension. Interactive window, notebook support, debugging. Popular for data science.
- **[Positron](https://github.com/posit-dev/positron)** (3.9k GitHub stars): Data science IDE by Posit. Built on Code OSS. Python and R, variable explorer, multi-session console, notebooks, plot pane, database pane. VS Code–compatible extensions.
- **PyCharm Professional**: Full-featured IDE with scientific tools. Interactive console, notebook support, data viewer. JetBrains IDE.
- **[Spyder](https://github.com/spyder-ide/spyder)** (9.1k GitHub stars): Scientific Python IDE. Variable explorer, IPython console, debugging tools. Designed for data science.
- **[RStudio (with reticulate)](https://github.com/rstudio/reticulate)** (1.7k GitHub stars): RStudio with Python support via reticulate. Good for R/Python hybrid workflows.
- **antigravity**: Google's Antigravity IDE. Browser-based development environment focused on Python and data workflows, with integrated tools for exploration, visualization, and experimentation.


### Specialized Interactive Tools
- **Databricks Notebooks**: Collaborative notebooks in Databricks. Spark integration, SQL support, version control.
- **Hex**: Modern data notebook. SQL + Python, collaborative, interactive visualizations. Cloud-based.
- **[Deepnote](https://github.com/deepnote/deepnote)** (2.6k GitHub stars): Collaborative data science notebook. Real-time collaboration, GPU access, integrations.
- **[Observable](https://github.com/observablehq/observable)** (5.1k GitHub stars): JavaScript-first notebook (with Python support). Reactive, interactive visualizations.
- **[Noteable](https://github.com/noteable-io)** (noteable-io organization): Collaborative notebook platform. Cloud-based notebook environment.
- **[Saturn Cloud](https://github.com/saturncloud)** (saturncloud organization): Cloud-based data science platform. Jupyter notebooks with GPU/CPU resources.
- **Paperspace Gradient**: Cloud notebooks with GPU. Machine learning development environment.
- **[CoCalc](https://github.com/sagemathinc/cocalc)** (1.3k GitHub stars): Collaborative computational environment. Real-time collaborative editing.
- **[nteract](https://github.com/nteract/nteract)** (6.3k GitHub stars): Desktop notebook application. Native desktop app for Jupyter notebooks.

### Notebook Tools
- **[jupyter-book](https://github.com/executablebooks/jupyter-book)** (4.2k GitHub stars): Build books from notebooks. Create publication-quality books from Jupyter notebooks.
- **[nbconvert](https://github.com/jupyter/nbconvert)** (1.9k GitHub stars): Convert notebooks to various formats. Part of Jupyter ecosystem.
- **[papermill](https://github.com/nteract/papermill)** (6.3k GitHub stars): Parameterize and execute notebooks. Run notebooks with different parameters.
- **[Quarto](https://github.com/quarto-dev/quarto-cli)** (5.1k GitHub stars): Scientific publishing system. Supports Jupyter notebooks, R Markdown, markdown. Reproducible research.

## Data Frames

### Core DataFrame Libraries
- **[Pandas](https://github.com/pandas-dev/pandas)** (47.7k GitHub stars): Most popular DataFrame library. Rich API, extensive functionality. Great for data analysis and manipulation.
- **[Polars](https://github.com/pola-rs/polars)** (37.3k GitHub stars): Fast DataFrame library written in Rust. Lazy evaluation, parallel processing. Much faster than Pandas for large datasets.
- **[Datatable](https://github.com/h2oai/datatable)** (1.9k GitHub stars): High-performance data manipulation. Fast operations on large datasets. R data.table port to Python.

### Distributed & Parallel Processing
- **[Dask](https://github.com/dask/dask)** (13.7k GitHub stars): Parallel computing library. Scales Pandas operations to multiple cores/clusters. Lazy evaluation.
- **[Modin](https://github.com/modin-project/modin)** (10.4k GitHub stars): Drop-in Pandas replacement. Automatically parallelizes operations. Uses Ray or Dask backend.
- **[Ray](https://github.com/ray-project/ray)** (41.1k GitHub stars): Distributed computing framework. Can be used with Modin for parallel DataFrame operations.
- **[Vaex](https://github.com/vaexio/vaex)** (8.5k GitHub stars): Out-of-core DataFrame library. Handles datasets larger than memory. Lazy evaluation, fast aggregations.

### In-Memory Analytical Databases
- **[DuckDB](https://github.com/duckdb/duckdb)** (35.8k GitHub stars): In-process analytical database. SQL interface, fast queries on Parquet/CSV. Can be used as DataFrame alternative.
- **[Polars](https://github.com/pola-rs/polars)** (37.3k GitHub stars): Also supports SQL queries via `polars.sql` (see Core DataFrame Libraries).

### Specialized DataFrame Libraries
- **[PyArrow](https://github.com/apache/arrow)** (16.5k GitHub stars): Columnar in-memory format. Foundation for many DataFrame libraries. Fast I/O, zero-copy reads.
- **[Apache Spark (PySpark)](https://github.com/apache/spark)** (42.7k GitHub stars): Distributed DataFrame API. For big data processing on clusters. Part of Apache Spark ecosystem.
- **[Koalas (Pandas API on Spark)](https://github.com/databricks/koalas)** (3.4k GitHub stars): Pandas-like API on Spark. Now part of PySpark as `pyspark.pandas`.
- **[Ibis](https://github.com/ibis-project/ibis)** (6.4k GitHub stars): Python dataframe library with SQL backends. Write DataFrame code, execute on databases.
- **Pandas-API**: Unified API across multiple DataFrame libraries (Pandas, Polars, PySpark, etc.). Write once, run anywhere.

### DataFrame Interoperability
- **[Pandas](https://github.com/pandas-dev/pandas)** (47.8k GitHub stars): Can read/write many formats (CSV, Parquet, Excel, JSON, SQL, etc.).
- **[Polars](https://github.com/pola-rs/polars)** (37.3k GitHub stars): Fast I/O, supports Parquet, CSV, JSON, Arrow, Excel. Can read from databases.
- **[PyArrow](https://github.com/apache/arrow)** (16.5k GitHub stars): Enables zero-copy data sharing between libraries. Used by Pandas, Polars, DuckDB.
- **[Fletcher](https://github.com/xhochy/fletcher)** (228 GitHub stars): Pandas extension for Apache Arrow. Efficient columnar operations.
- **[Narwhals](https://github.com/prefix-dev/narwhals)** (1.5k GitHub stars): Lightweight compatibility layer between dataframe libraries. Write dataframe-agnostic code that works with Pandas, Polars, PyArrow, cuDF, Modin, Dask, DuckDB, and more.
- **[pyjanitor](https://github.com/pyjanitor-devs/pyjanitor)** (1.5k GitHub stars): Data cleaning library (pandas extension). Clean APIs for data cleaning tasks. Python implementation of R package Janitor.
- **[skrub](https://github.com/skrub-data/skrub)** (1.5k GitHub stars): Prepare tabular data for ML. TableVectorizer, encoding for messy strings/categoricals, fuzzy joining, Cleaner, TableReport. Scikit-learn–compatible, works with pandas and polars. Formerly dirty_cat.

### Time-Series DataFrames
- **[xarray](https://github.com/pydata/xarray)** (4k GitHub stars): Labeled multi-dimensional arrays, great for time-series data. Works with pandas for time-series operations. Also useful for geospatial/raster data.
- **[Prophet](https://github.com/facebook/prophet)** (20k GitHub stars): Facebook's time series forecasting tool. Produces high-quality forecasts for time series data with multiple seasonality. Robust to outliers, missing data, and trend changes.
- **[sktime](https://github.com/sktime/sktime)** (9.4k GitHub stars): Unified framework for machine learning with time series. Offers forecasting pipelines and composition tools. Scikit-learn compatible.
- **[tsfresh](https://github.com/blue-yonder/tsfresh)** (9.1k GitHub stars): Automatic extraction of relevant features from time series data. Complements forecasting libraries like Prophet.
- **[statsforecast](https://github.com/nixtla/statsforecast)** (4.6k GitHub stars): Lightning-fast forecasting library with statistical and econometric models. By Nixtla.
- **[pandas-ta](https://github.com/twopirllc/pandas-ta)** (6.1k GitHub stars): Technical analysis indicators for time series. Pandas extension for technical analysis.

### GPU-Accelerated DataFrames
- **[cuDF (RAPIDS)](https://github.com/rapidsai/cudf)** (9.5k GitHub stars): GPU-accelerated DataFrame library. Pandas-like API, runs on NVIDIA GPUs. Part of RAPIDS ecosystem.
- **[Polars](https://github.com/pola-rs/polars)** (37.3k GitHub stars): Can use GPU acceleration in some operations (experimental).

### DataFrame Validation & Testing
- **[Pandera](https://github.com/unionai/pandera)** (4.2k GitHub stars): DataFrame validation library. Schema validation, data quality checks. Works with Pandas, Polars, Dask.
- **[Great Expectations](https://github.com/great-expectations/great_expectations)** (11.1k GitHub stars): Data validation and testing framework. Works with Pandas, Spark, SQL databases.
- **[Pointblank](https://posit.co/blog/introducing-pointblank-for-python/)** (332 GitHub stars): Data validation and testing library from Posit (formerly RStudio). Works with Pandas, Polars, DuckDB, ....


### Polars Ecosystem

- **[Awesome Polars](https://github.com/ddotta/awesome-polars)** (1k GitHub stars): A curated list of awesome Polars libraries, resources, and tools.
- **[Official site](https://docs.pola.rs/user-guide/ecosystem/)**: Official documentation for the Polars ecosystem.



## Statistics

### Core and Classical Statistics
- **[Statsmodels](https://github.com/statsmodels/statsmodels)** (11.2k GitHub stars): Statistical modeling and econometrics.
- **[Patsy](https://github.com/pydata/patsy)** (978 GitHub stars): Statistical formulas and model specification.
- **[Pingouin](https://github.com/raphaelvallat/pingouin)** (1.9k GitHub stars): Statistical package built on Pandas. Easy-to-use functions for common statistical analyses including ANOVAs, ANCOVAs, post-hoc tests, non-parametric tests, Bayesian T-tests, and more.
- **[scipy.stats](https://github.com/scipy/scipy)** (14.3k GitHub stars): Statistical functions (part of scipy, see Algebra section).
- **[researchpy](https://github.com/researchpy/researchpy)** (326 GitHub stars): Statistical analysis library. Additional statistical functions and tests.
- **[pyvttbl](https://github.com/statmodels/pyvttbl)** (82 GitHub stars): Analysis of variance library. Statistical analysis tools.

### Bayesian Statistics
- **[PyMC](https://github.com/pymc-devs/pymc)** (9.5k GitHub stars): Probabilistic programming and Bayesian modeling. MCMC (NUTS), variational inference, PyTensor backend. Integrates with ArviZ and Bambi.
- **[ArviZ](https://github.com/arviz-devs/arviz)** (1.8k GitHub stars): Backend-agnostic diagnostics and visualization for Bayesian inference. Works with PyMC, CmdStanPy, Pyro, NumPyro, emcee.
- **[Bambi](https://github.com/bambinos/bambi)** (1.2k GitHub stars): High-level Bayesian model-building with formula syntax (PyMC-based). Mixed-effects, GLMs, hierarchical models.
- **[preliz](https://github.com/arviz-devs/preliz)** (133 GitHub stars): Prior elicitation and exploring probability distributions. Interactive viz. Usable with PyMC/PyStan.

### Econometrics
- **[linearmodels](https://github.com/bashtage/linearmodels)** (1k GitHub stars): Instrumental variables (2SLS, GMM), panel (fixed/random effects, Fama–MacBeth), SUR, 3SLS. Extends statsmodels.
- **[arch](https://github.com/bashtage/arch)** (1.5k GitHub stars): ARCH/GARCH and related volatility models. Unit-root tests, model confidence sets. Used in financial econometrics.

### Survival Analysis
- **[lifelines](https://github.com/CamDavidsonPilon/lifelines)** (2.5k GitHub stars): Survival and duration analysis. Kaplan–Meier, Nelson–Aalen, parametric and semi-parametric models, censoring. Pure Python, pandas-friendly.

### Causal Inference
- **[DoWhy](https://github.com/py-why/dowhy)** (6.8k GitHub stars): End-to-end causal inference. Model, identify, estimate, refute. Graphical causal models and potential outcomes. Part of PyWhy ecosystem.
- **[EconML](https://github.com/py-why/econml)** (7.2k GitHub stars): Microsoft's library for heterogeneous treatment effects. CATE estimation, instrumental variables, policy learning. Integrates with DoWhy.

### Statistical Annotations and Post-Hoc
- **[statannotations](https://github.com/trevismd/statannotations)** (822 GitHub stars): Add statistical test annotations (p-values, stars) to seaborn figures (box, bar, violin, etc.). Multiple-test correction options.

## Signal Processing

### General Signal Processing
- **scipy.signal**: Convolution, correlation, filtering (median, Wiener, order), B-splines. Part of SciPy (see Algebra section).
- **scipy.fft**: Fast Fourier Transform and related. Part of SciPy.

### Audio & Music
- **[librosa](https://github.com/librosa/librosa)** (8.1k GitHub stars): Audio and music analysis. Spectral representations, chromagrams, Mel spectrograms, MFCCs, beat/tempo, onset detection, harmonic-percussive separation. Integrates with NumPy/SciPy.
- **[soundfile](https://github.com/bastibe/python-soundfile)** (1.5k GitHub stars): Audio I/O based on libsndfile. Read/write WAV, FLAC, OGG, etc. Returns NumPy arrays.

### Wavelets & Transforms
- **[PyWavelets](https://github.com/PyWavelets/pywt)** (2.3k GitHub stars): Discrete wavelet transforms. DWT, IDWT, wavelet packets. Production-stable.

### Domain-Specific
- **[ObsPy](https://github.com/obspy/obspy)** (1.2k GitHub stars): Seismological data processing. Parsers for common formats, data-center clients, seismological signal routines for time series.

## Classic ML

### Core ML Libraries
- **[Scikit-learn](https://github.com/scikit-learn/scikit-learn)** (64.9k GitHub stars): Most popular machine learning library. Comprehensive tools for classification, regression, clustering, and more.
- **[XGBoost](https://github.com/dmlc/xgboost)** (27.9k GitHub stars): Gradient boosting framework. Fast and efficient.
- **[LightGBM](https://github.com/microsoft/LightGBM)** (18k GitHub stars): Gradient boosting framework by Microsoft. Fast training and high accuracy.
- **[CatBoost](https://github.com/catboost/catboost)** (8.7k GitHub stars): Gradient boosting framework. Handles categorical features automatically.
- **[Optuna](https://github.com/optuna/optuna)** (13.5k GitHub stars): Hyperparameter optimization framework. Automatic hyperparameter tuning.

### Specialized ML Libraries
- **[imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn)** (7.1k GitHub stars): Python package for handling imbalanced datasets in machine learning. Resampling techniques and metrics.
- **[scikit-image](https://github.com/scikit-image/scikit-image)** (6.4k GitHub stars): Image processing library in Python. Part of scikit-learn ecosystem.
- **[mlxtend](https://github.com/rasbt/mlxtend)** (5.1k GitHub stars): Library of extension and helper modules for Python's data analysis and machine learning libraries.

### Model Interpretability
- **[shap](https://github.com/slundberg/shap)** (25k GitHub stars): SHAP (SHapley Additive exPlanations) values for model interpretation. Game theoretic approach to explain the output of any machine learning model.
- **[lime](https://github.com/marcotcr/lime)** (12.1k GitHub stars): LIME (Local Interpretable Model-agnostic Explanations). Explaining the predictions of any machine learning classifier.
- **[knockpy](https://amspector100.github.io/knockpy/)**: Implements the knockoff filter framework for feature selection. Akin to permutation importance, only that it accounts for the correlation structure of the features.
- **[eli5](https://github.com/TeamHG-Memex/eli5)** (2.8k GitHub stars): Library for debugging and inspecting machine learning classifiers and explaining predictions.
- **[yellowbrick](https://github.com/DistrictDataLabs/yellowbrick)** (4.4k GitHub stars): ML visualization suite. Visual analysis and diagnostic tools for feature selection, model selection, and parameter tuning.

### AutoML
- **[auto-sklearn](https://github.com/automl/auto-sklearn)** (8k GitHub stars): Automated ML with meta-learning. Drop-in scikit-learn replacement. Bayesian optimization, ensemble construction.
- **[FLAML](https://github.com/microsoft/FLAML)** (4.3k GitHub stars): Fast and lightweight AutoML by Microsoft. Efficient hyperparameter tuning and model selection. Scikit-learn compatible.
- **[TPOT](https://github.com/EpistasisLab/tpot)** (9.5k GitHub stars): Genetic programming for AutoML. Automatically designs and optimizes ML pipelines. Built on scikit-learn.
- **H2O AutoML**: Automated ML from H2O.ai. Python API for automatic model training and selection. Part of H2O-3 ecosystem.

### Recommendation Systems
- **[Surprise](https://github.com/NicolasHug/Surprise)** (6.8k GitHub stars): Building and analyzing recommender systems. SVD, NMF, collaborative filtering. Built-in datasets (MovieLens, Jester), cross-validation.
- **[implicit](https://github.com/benfred/implicit)** (3.5k GitHub stars): Fast collaborative filtering for implicit feedback. ALS, BPR, Logistic Matrix Factorization. GPU support, Cython-optimized.

### Anomaly Detection
- **[PyOD](https://github.com/yzhao062/pyod)** (9.7k GitHub stars): Comprehensive anomaly detection. 45+ algorithms (classical and deep learning). Unified API, scikit-learn compatible. ADBench benchmarking.

### Feature Engineering
- **[Featuretools](https://github.com/alteryx/featuretools)** (7.6k GitHub stars): Automated feature engineering from relational and temporal data. Deep Feature Synthesis. Multi-table, time-aware feature generation.

## NLP

### Core NLP Libraries
- **[spaCy](https://github.com/explosion/spaCy)** (30.2k GitHub stars): Production-focused NLP library. Fast tokenization, NER, dependency parsing, pre-trained models for many languages. Modern alternative to NLTK.
- **[NLTK](https://github.com/nltk/nltk)** (13.2k GitHub stars): Classic NLP toolkit for research and education. Tokenization, parsing, POS tagging, corpora. Extensive documentation and resources.
- **[Gensim](https://github.com/RaRe-Technologies/gensim)** (15.4k GitHub stars): Topic modeling (LDA), word embeddings (Word2Vec, FastText), document similarity. Unsupervised NLP for semantic analysis.
- **[TextBlob](https://github.com/sloria/TextBlob)** (9.2k GitHub stars): Simple NLP for sentiment analysis, POS tagging, noun phrase extraction. Built on NLTK and Pattern. Easy API for quick text processing.
- **[Stanza](https://github.com/stanfordnlp/stanza)** (7.2k GitHub stars): Stanford NLP Python port. Full neural pipeline for 66+ languages. Tokenization, POS, NER, dependency parsing, sentiment.

## Computer Vision

### Core Image Libraries
- **[OpenCV](https://github.com/opencv/opencv)** (80.2k GitHub stars): The standard computer vision library. Image I/O, filtering, feature detection, object detection, video processing. C++ core with Python bindings.
- **[Pillow](https://github.com/python-pillow/Pillow)** (12.8k GitHub stars): Image loading, resizing, format conversion. PIL fork; often the first library for basic image handling. Supports many formats.
- **[albumentations](https://github.com/albumentations-team/albumentations)** (14.2k GitHub stars): Image augmentation for ML. Used with PyTorch/TensorFlow. Fast, flexible augmentations for training pipelines.
- **[kornia](https://github.com/kornia/kornia)** (9.4k GitHub stars): Differentiable computer vision (PyTorch). Geometric transforms, feature detection, depth estimation. GPU-accelerated, differentiable ops.

## Deep Learning

### Core Deep Learning Frameworks
- **[PyTorch](https://github.com/pytorch/pytorch)** (96.8k GitHub stars): Most popular deep learning framework. Dynamic computation graphs, great for research.
- **[TensorFlow](https://github.com/tensorflow/tensorflow)** (193k GitHub stars): Google's deep learning framework. Production-ready, supports both eager and graph execution.
- **[Keras](https://github.com/keras-team/keras)** (61.2k GitHub stars): High-level neural networks API. Runs on top of TensorFlow, JAX, or PyTorch.
- **[Hugging Face Transformers](https://github.com/huggingface/transformers)** (156k GitHub stars): State-of-the-art NLP models. Pre-trained transformers for various tasks.
- **[Hugging Face Accelerate](https://github.com/huggingface/accelerate)** (9.5k GitHub stars): Library for easy multi-GPU/TPU training. Simplifies distributed training.

### High-Level Deep Learning Libraries
- **[PyTorch Lightning](https://github.com/Lightning-AI/pytorch-lightning)** (30.8k GitHub stars): Framework for pretraining and finetuning AI models. High-level PyTorch wrapper with zero code changes needed for scaling.
- **[FastAI](https://github.com/fastai/fastai)** (27.8k GitHub stars): High-level deep learning library. Makes deep learning more accessible. Built on PyTorch.

### Model Formats & Tools
- **[ONNX](https://github.com/onnx/onnx)** (20.2k GitHub stars): Open Neural Network Exchange format. Interoperability between different deep learning frameworks.
- **[TensorBoard](https://github.com/tensorflow/tensorboard)** (7.1k GitHub stars): Visualization toolkit for TensorFlow. Part of TensorFlow ecosystem. Model visualization and monitoring.

### Experiment Tracking
- **[Weights & Biases (wandb)](https://github.com/wandb/wandb)** (10.8k GitHub stars): Experiment tracking platform. Integrated with PyTorch Lightning and other frameworks.
- **[MLflow](https://github.com/mlflow/mlflow)** (23.8k GitHub stars): ML lifecycle management and experiment tracking. Open-source platform.
- **[Neptune](https://github.com/neptune-ai/neptune-client)** (1.4k GitHub stars): Experiment tracking platform. MLOps tool for managing experiments.
- **[Comet](https://github.com/comet-ml/comet-llm)** (1.2k GitHub stars): ML experiment tracking. Model management and monitoring.

### Hyperparameter Tuning
- **[Keras Tuner](https://github.com/keras-team/keras-tuner)** (2.5k GitHub stars): Hyperparameter tuning for Keras. Automated hyperparameter search.
- **[Ray Tune](https://github.com/ray-project/ray)** (41.1k GitHub stars): Hyperparameter tuning (part of Ray, see Distributed & Parallel Processing). Scalable hyperparameter search.

## Reinforcement Learning

### Environments
- **[Gymnasium](https://github.com/Farama-Foundation/Gymnasium)** (4.2k GitHub stars): API standard for single-agent RL environments. Successor to OpenAI Gym; maintained by Farama Foundation. Classic Control, Atari, MuJoCo, Box2D, Toy Text. Common interface for training libraries.
- **[PettingZoo](https://github.com/Farama-Foundation/PettingZoo)** (2.2k GitHub stars): Multi-agent RL environments. Same API style as Gymnasium; multi-agent games and benchmarks. By Farama Foundation.
- **[MinAtar](https://github.com/kenjyoung/MinAtar)** (500+ GitHub stars): Minimalist Atari-like environments. Fast, lightweight; good for prototyping and research.

### Core Algorithm Libraries
- **[RLlib](https://github.com/ray-project/ray)** (41.1k GitHub stars): Distributed RL library (part of Ray). Scalable training; many algorithms, multi-agent, offline RL. Uses Gymnasium/PettingZoo for environments.
- **[Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3)** (12.6k GitHub stars): Reliable implementations of deep RL algorithms (PPO, SAC, A2C, DQN, etc.). PyTorch-based; works with Gymnasium. Benchmarked, well-documented.
- **[CleanRL](https://github.com/CleanRL/CleanRL)** (5.2k GitHub stars): Clean, single-file implementations of deep RL algorithms. Research-friendly; minimal dependencies, easy to read and modify. TensorBoard, W&B; supports Gymnasium.
- **[Dopamine](https://github.com/google/dopamine)** (10.5k GitHub stars): Research framework for fast prototyping of RL algorithms. By Google. Focus on reproducibility and ablation; JAX-based (Dopamine 2.x).
- **[SB3-Contrib](https://github.com/Stable-Baselines-Team/stable-baselines3-contrib)** (688 GitHub stars): Extra algorithms and features for Stable-Baselines3. Experimental (TQC, QRDQN, etc.).

### Transformer & LLM Reinforcement Learning (RLHF, etc.)
- **[TRL](https://github.com/huggingface/trl)** (10.5k GitHub stars): Transformer Reinforcement Learning. Train and align LLMs with RL: SFT, DPO, PPO, GRPO, reward modeling, KTO, ORPO. Integrates with Hugging Face Transformers and PEFT.
- **[axolotl](https://github.com/OpenAccess-AI-Collective/axolotl)** (8k+ GitHub stars): LLM fine-tuning and RLHF. SFT, LoRA, DPO, and related methods; YAML config, multi-framework support.
- **[OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)** (6k+ GitHub stars): Open-source RLHF stack. Train reward models and policy with PPO; supports LLaMA, ChatGLM, and others.

## Agents

- **[Smolagents](https://github.com/huggingface/smolagents)** (24.6k GitHub stars): Small language agents. By Hugging Face. Good for small tasks.
- **[Pydantic-ai](https://github.com/pydantic/pydantic-ai)** (14.4k GitHub stars): Type-safe AI agent framework. Structured outputs, Pydantic validation, model-agnostic. By Pydantic.
- **[LangChain](https://github.com/langchain-ai/langchain)** (125k GitHub stars): Framework for building applications with LLMs, chains, and agents. Most popular agent framework.
- **[LangGraph](https://github.com/langchain-ai/langgraph)** (23.8k GitHub stars): Stateful, multi-actor applications with LLMs. Built on LangChain for complex agent workflows.
- **[AutoGen](https://github.com/microsoft/autogen)** (49.2k GitHub stars): Multi-agent conversation framework by Microsoft. Enables multiple agents to collaborate.
- **[CrewAI](https://github.com/joaomdmoura/crewAI)** (37.9k GitHub stars): Framework for orchestrating role-playing, autonomous AI agents that collaborate.
- **[LlamaIndex](https://github.com/run-llama/llama_index)** (46.5k GitHub stars): Data framework for LLM applications. Focus on RAG and data ingestion.
- **[Semantic Kernel](https://github.com/microsoft/semantic-kernel)** (27.1k GitHub stars): Microsoft's AI orchestration framework for integrating LLMs into applications.
- **[Haystack](https://github.com/deepset-ai/haystack)** (23.9k GitHub stars): End-to-end NLP framework with agent capabilities. By deepset.
- **[AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)** (181k GitHub stars): Autonomous agent framework for goal-oriented tasks.
- **[BabyAGI](https://github.com/yoheinakajima/babyagi)** (22.1k GitHub stars): Task-driven autonomous agent system.
- **[AgentGPT](https://github.com/reworkd/AgentGPT)** (35.5k GitHub stars): Browser-based agent framework.
- **OpenAI Assistants API**: OpenAI's native agent framework with function calling and tools.
- **ReAct**: Reasoning and acting framework. Combines reasoning and acting in language models.

### AI CLI Assistants
- **[Claude Code](https://github.com/anthropics/claude-code)** (61k+ GitHub stars): Agentic coding tool that runs in your terminal. Understands your codebase, helps with edits, explanations, and git workflows via the `claude` CLI.
- **[aider](https://github.com/Aider-AI/aider)** (39.9k GitHub stars): AI pair‑programmer for your terminal. Chat‑based CLI that edits your codebase with strong git integration and support for many LLMs.
- **[Open Interpreter](https://github.com/openinterpreter/open-interpreter)** (61.8k GitHub stars): Natural‑language interface to your computer in the terminal. Lets models run code, control tools, and work with files and browsers.
- **[Warp](https://github.com/warpdotdev/Warp)** (25.7k GitHub stars): Modern GPU‑accelerated terminal with built‑in AI agents (Claude and others). Agentic development environment for shell workflows and code tasks.




## GIS

### Core Data Manipulation
- **[GeoPandas](https://github.com/geopandas/geopandas)** (5k GitHub stars): Extends Pandas to work with geospatial data. Most popular GIS library in Python.
- **[Shapely](https://github.com/shapely/shapely)** (4.4k GitHub stars): Geometric operations, spatial predicates, and geometric analysis (point-in-polygon, buffers, intersections).
- **[Fiona](https://github.com/Toblerity/Fiona)** (1.2k GitHub stars): Reading and writing spatial data files (shapefiles, GeoJSON, etc.). Built on GDAL.
- **[PyShp](https://github.com/GeospatialPython/pyshp)** (1.1k GitHub stars): Pure Python library for reading and writing shapefiles.

### Coordinate Systems & Geocoding
- **[GeoPy](https://github.com/geopy/geopy)** (4.8k GitHub stars): Geocoding library for finding coordinates of addresses and vice versa.
- **[PyProj](https://github.com/pyproj4/pyproj)** (1.2k GitHub stars): Cartographic projections and coordinate transformations (PROJ library wrapper).

### Raster Processing
- **[Rasterio](https://github.com/rasterio/rasterio)** (2.5k GitHub stars): Reading and writing geospatial raster data.
- **[GDAL/OGR](https://github.com/OSGeo/gdal)** (5.7k GitHub stars): Python bindings for GDAL (Geospatial Data Abstraction Library). Powerful but lower-level.
- **[Rioxarray](https://github.com/corteva/rioxarray)** (594 GitHub stars): Combines Rasterio with xarray for labeled raster arrays.
- **[RasterStats](https://github.com/perrygeo/python-raster-stats)** (553 GitHub stars): Zonal statistics and raster analysis.
- **[xarray](https://github.com/pydata/xarray)** (4k GitHub stars): Labeled multi-dimensional arrays for raster/time-series geospatial data (also in Time-Series DataFrames section).

### Spatial Analysis
- **[OSMnx](https://github.com/gboeing/osmnx)** (5.5k GitHub stars): Downloading, modeling, analyzing, and visualizing street networks from OpenStreetMap.
- **[NetworkX](https://github.com/networkx/networkx)** (16.5k GitHub stars): Network analysis (often used with OSMnx for routing).
- **[PySAL](https://github.com/pysal/pysal)** (1.5k GitHub stars): Python Spatial Analysis Library. Collection of spatial analysis functions.
- **[Libpysal](https://github.com/pysal/libpysal)** (270 GitHub stars): Core components of PySAL ecosystem.
- **[Esda](https://github.com/pysal/esda)** (222 GitHub stars): Exploratory spatial data analysis.
- **[Splot](https://github.com/pysal/splot)** (101 GitHub stars): Spatial visualization and plotting.
- **[whitebox](https://github.com/opengeos/whitebox-python)** (1.2k GitHub stars): Advanced geospatial analysis tools. Comprehensive suite of geospatial analysis functions.

### Visualization & Mapping
- **[Folium](https://github.com/python-visualization/folium)** (7.3k GitHub stars): Interactive maps using Leaflet.js. Great for web maps.
- **[Contextily](https://github.com/geopandas/contextily)** (573 GitHub stars): Add basemaps to matplotlib/geopandas plots.
- **[Geoplotlib](https://github.com/andrea-cuttone/geoplotlib)** (1k GitHub stars): Geographic data visualization toolkit.
- **[Geoviews](https://github.com/holoviz/geoviews)** (624 GitHub stars): Interactive geospatial visualizations with HoloViews.
- **[Cartopy](https://github.com/SciTools/cartopy)** (1.6k GitHub stars): Cartographic projections and mapping (matplotlib extension).

### Remote Sensing & Satellite Data
- **[Rasterio](https://github.com/rasterio/rasterio)** (2.5k GitHub stars): Raster data I/O.
- **[Sentinelsat](https://github.com/sentinelsat/sentinelsat)** (1k GitHub stars): Search and download Sentinel satellite imagery.
- **[Landsat-util](https://github.com/developmentseed/landsat-util)** (690 GitHub stars): Landsat satellite imagery utilities.
- **[Py6S](https://github.com/robintw/Py6S)** (179 GitHub stars): Atmospheric correction for satellite imagery.

### Routing & Network Analysis
- **[OSMnx](https://github.com/gboeing/osmnx)** (5.5k GitHub stars): Street network analysis.
- **[NetworkX](https://github.com/networkx/networkx)** (16.5k GitHub stars): Graph and network analysis.
- **[Routingpy](https://github.com/GIScience/routingpy)** (330 GitHub stars): Routing engine clients (OSRM, GraphHopper, etc.).

### Database Integration
- **[GeoAlchemy2](https://github.com/geoalchemy/geoalchemy2)** (692 GitHub stars): Spatial extensions for SQLAlchemy (PostGIS support).
- **[Psycopg2](https://github.com/psycopg/psycopg2)** (4k GitHub stars): PostgreSQL adapter (for PostGIS databases).




## Visualization

### General Visualization
- **[Plotly Express](https://github.com/plotly/plotly.py)** (18.2k GitHub stars): High-level interface to Plotly. Easy-to-use plotting.
- **[Plotly Graph Objects](https://github.com/plotly/plotly.py)** (18.2k GitHub stars): Low-level interface to Plotly. More control over plots.
- **[Altair](https://github.com/vega/altair)** (10.1k GitHub stars): Declarative statistical visualization. Grammar of graphics.
- **[Seaborn](https://github.com/mwaskom/seaborn)** (13.7k GitHub stars): Statistical data visualization. Built on matplotlib.
- **[Matplotlib](https://github.com/matplotlib/matplotlib)** (22.3k GitHub stars): Most popular plotting library. Comprehensive 2D plotting.
- **[Plotnine](https://github.com/has2k1/plotnine)** (4.5k GitHub stars): Grammar of graphics for Python. ggplot2 port.
- **[Bokeh](https://github.com/bokeh/bokeh)** (19k GitHub stars): Interactive visualization library. Great for web applications.
- **[Holoviews](https://github.com/holoviz/holoviews)** (2.9k GitHub stars): High-level visualization library. Declarative plotting.
- **[Datashader](https://github.com/holoviz/datashader)** (3.2k GitHub stars): Rasterization pipeline for large datasets. Fast visualization of big data.

### Specialized Visualization
- **[missingno](https://github.com/ResidentMario/missingno)** (3.5k GitHub stars): Visualize missing data patterns. Matrix plots, bar charts, and heatmaps for missing data.
- **[yellowbrick](https://github.com/DistrictDataLabs/yellowbrick)** (4.4k GitHub stars): ML visualization suite (also in Classic ML section). Visual analysis tools for ML.
- **[wordcloud](https://github.com/amueller/word_cloud)** (10.5k GitHub stars): Word cloud generation library. Create word clouds from text.
- **[Great Tables](https://github.com/posit-dev/great-tables)** (2.6k GitHub stars): Publication-quality display tables from Pandas or Polars DataFrames. Headers, footers, formatting, styling. Renders to HTML or images. By Posit.
- **[mplfinance](https://github.com/matplotlib/mplfinance)** (1.1k GitHub stars): Financial plotting library. Candlestick charts, technical indicators.
- **[pygal](https://github.com/Kozea/pygal)** (3.2k GitHub stars): SVG charting library. Create interactive SVG charts.
- **[graphviz](https://github.com/xflr6/graphviz)** (1k GitHub stars): Graph visualization library. Create and render graph structures.

### Geographic Visualization
- **[Geoplotlib](https://github.com/andrea-cuttone/geoplotlib)** (1k GitHub stars): Geographic data visualization toolkit.
- **[Geoviews](https://github.com/holoviz/geoviews)** (624 GitHub stars): Interactive geospatial visualizations with HoloViews.
- **[Cartopy](https://github.com/SciTools/cartopy)** (1.6k GitHub stars): Cartographic projections and mapping (matplotlib extension).
- **[Folium](https://github.com/python-visualization/folium)** (7.3k GitHub stars): Interactive maps using Leaflet.js. Great for web maps.



## Algebra

### Core Numerical Computing
- **[Numpy](https://github.com/numpy/numpy)** (31.3k GitHub stars): Numerical computing. Foundation for scientific Python.
- **[Scipy](https://github.com/scipy/scipy)** (14.3k GitHub stars): Scientific computing. Built on NumPy, includes optimization, integration, interpolation, etc.
- **[Sympy](https://github.com/sympy/sympy)** (14.3k GitHub stars): Symbolic computing. Computer algebra system.
- **[mlx](https://github.com/ml-explore/mlx)** (23.5k GitHub stars): Apple's linear algebra. Optimized for Apple Silicon.
- **[JAX](https://github.com/google/jax)** (28.9k GitHub stars): Automatic differentiation and numerical computing. NumPy-compatible with GPU/TPU support.
- **[PyTorch](https://github.com/pytorch/pytorch)** (96.8k GitHub stars): Deep learning framework with tensor operations (also in Deep Learning section).

### Performance & GPU Acceleration
- **[CuPy](https://github.com/cupy/cupy)** (10.7k GitHub stars): NumPy-compatible GPU array library. NumPy for the GPU with nearly identical API. Runs on NVIDIA GPUs.
- **[Numba](https://github.com/numba/numba)** (10.9k GitHub stars): JIT (Just-In-Time) compiler that translates a subset of Python and NumPy code into fast machine code using LLVM. NumPy-aware dynamic Python compiler.
- **[Cython](https://github.com/cython/cython)** (9.2k GitHub stars): C extensions for Python. Used for performance optimization. Compile Python-like code to C.
- **[Theano](https://github.com/Theano/Theano)** (11.2k GitHub stars): (Deprecated) Historical deep learning library. No longer maintained but was influential in the development of modern deep learning frameworks. 

## DataBases

### ORMs (Object-Relational Mappers)
- **[SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)** (11.4k GitHub stars): Most popular Python ORM. Powerful, flexible, supports multiple databases. Core and ORM layers.
- **[Django ORM](https://github.com/django/django)** (86.5k GitHub stars): Built into Django framework. Easy to use, migrations included. Great for Django projects.
- **[Peewee](https://github.com/coleifer/peewee)** (11.9k GitHub stars): Lightweight ORM. Simple API, small footprint. Good for small to medium projects.
- **[Tortoise ORM](https://github.com/tortoise/tortoise-orm)** (5.4k GitHub stars): Async ORM inspired by Django. Built for async/await. Supports PostgreSQL, MySQL, SQLite.
- **[SQLModel](https://github.com/tiangolo/sqlmodel)** (17.5k GitHub stars): Modern ORM by FastAPI creator. Combines SQLAlchemy with Pydantic. Type-safe, auto-completion.
- **[Databases](https://github.com/encode/databases)** (4k GitHub stars): Async database library. Works with SQLAlchemy Core. Supports async operations.
- **[Pony ORM](https://github.com/ponyorm/pony)** (3.8k GitHub stars): ORM with Pythonic query syntax. Automatic query optimization. Good for complex queries.
- **[SQLObject](https://github.com/sqlobject/sqlobject)** (578 GitHub stars): Alternative ORM. Object-relational mapper with a different approach.
- **Storm**: ORM for Python. Database abstraction layer.

### Database Drivers & Adapters
- **sqlite3**: Built-in SQLite database (Python standard library). No installation needed.
- **Psycopg2/Psycopg3**: PostgreSQL adapter. Psycopg2 is mature, psycopg3 is modern async version.
- **pg8000**: Pure Python PostgreSQL driver. No C dependencies.
- **PyMySQL**: Pure Python MySQL client. No C dependencies. Good for compatibility.
- **mysql-connector-python**: Official MySQL connector. Full MySQL protocol support.
- **aiomysql**: Async MySQL driver. Built on PyMySQL. For async applications.
- **asyncpg**: Fast async PostgreSQL driver. High performance, no ORM overhead.
- **aiosqlite**: Async SQLite driver. For async SQLite operations.
- **pymongo**: Official MongoDB driver. Full MongoDB feature support.
- **motor**: Async MongoDB driver. Built on PyMongo. For async applications.
- **redis-py**: Redis client library. Supports all Redis commands.
- **aioredis**: Async Redis client. For async Redis operations.
- **cx_Oracle**: Oracle database adapter. Official Oracle driver.
- **pyodbc**: ODBC database connector. Works with SQL Server, Access, and other ODBC databases.
- **pymssql**: Microsoft SQL Server driver. Pure Python implementation.

### Query Builders & SQL Tools
- **[Records](https://github.com/kennethreitz/records)** (7.2k GitHub stars): Simple SQL query interface. Returns results as named tuples or dictionaries.
- **[Dataset](https://github.com/pudo/dataset)** (5k GitHub stars): Simple database abstraction. Works with SQLite, PostgreSQL, MySQL. Great for data science.
- **[Pypika](https://github.com/kayak/pypika)** (2.9k GitHub stars): SQL query builder. Write SQL queries in Python. Database agnostic.
- **[SQLGlot](https://github.com/tobymao/sqlglot)** (8.8k GitHub stars): SQL parser, transpiler, and optimizer. Parse and transform SQL across dialects.

### Connection Pooling & Management
- **DBUtils**: Database connection pooling utilities. Works with various database drivers.
- **SQLAlchemy Pool**: Built-in connection pooling in SQLAlchemy. Efficient connection management.

### Migration Tools
- **[Alembic](https://github.com/sqlalchemy/alembic)** (3.9k GitHub stars): Database migration tool for SQLAlchemy. Version control for database schemas.
- **[Django Migrations](https://github.com/django/django)** (86.5k GitHub stars): Built-in migration system for Django. Automatic migration generation.
- **[yoyo-migrations](https://github.com/ollyc/yoyo)** (1.2k GitHub stars): Database migration tool. Database agnostic, simple to use.

### Data Integration & ETL
- **[SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)** (11.4k GitHub stars): Can be used for ETL operations with its Core layer.
- **[Pandas](https://github.com/pandas-dev/pandas)** (47.8k GitHub stars): Read/write to databases via SQLAlchemy or direct drivers. Great for data analysis workflows.
- **[Polars](https://github.com/pola-rs/polars)** (37.3k GitHub stars): Fast DataFrame library with database integration. Can query databases directly.
- **[DuckDB](https://github.com/duckdb/duckdb)** (35.8k GitHub stars): In-process analytical database. Can query Parquet, CSV, and other formats. SQL interface.
- **[ConnectorX](https://github.com/sfu-db/connector-x)** (2.5k GitHub stars): Fast library for loading data from databases to DataFrames. Supports PostgreSQL, MySQL, SQLite, SQL Server, Oracle. Works with Pandas, PyArrow, Modin, Dask, Polars.
- **[dbc](https://github.com/prefix-dev/dbc)** (79 GitHub stars): Command-line tool for installing and managing ADBC (Apache Arrow Database Connectivity) drivers. Works on macOS, Linux, and Windows. Supports reproducible project environments with driver lists and lockfiles.
- **[Airflow](https://github.com/apache/airflow)** (43.9k GitHub stars): Apache Airflow - platform to programmatically author, schedule, and monitor workflows. Industry standard for workflow orchestration.
- **[Prefect](https://github.com/PrefectHQ/prefect)** (21.4k GitHub stars): Modern workflow orchestration framework for building resilient data pipelines. Python-first development with dynamic workflows.
- **[Luigi](https://github.com/spotify/luigi)** (18.6k GitHub stars): Python module for building complex pipelines of batch jobs. Handles dependency resolution, workflow management, visualization. Built-in Hadoop support.
- **[Bonobo](https://github.com/python-bonobo/bonobo)** (1.9k GitHub stars): ETL framework for Python. Simple, lightweight, and extensible.

### NoSQL & Document Databases
- **[pymongo](https://github.com/mongodb/mongo-python-driver)** (1k GitHub stars): MongoDB driver (see Database Drivers).
- **[motor](https://github.com/mongodb/motor)** (2.5k GitHub stars): Async MongoDB driver (see Database Drivers).
- **[cassandra-driver](https://github.com/datastax/python-driver)** (1.4k GitHub stars): Apache Cassandra driver. For distributed NoSQL databases.
- **[elasticsearch-py](https://github.com/elastic/elasticsearch-py)** (4.4k GitHub stars): Elasticsearch client. For search and analytics.
- **[neo4j](https://github.com/neo4j/neo4j-python-driver)** (1k GitHub stars): Neo4j graph database driver. For graph databases.

### Time-Series Databases
- **[influxdb-client](https://github.com/influxdata/influxdb-client-python)** (788 GitHub stars): InfluxDB client library. For time-series data.
- **[timescaledb](https://github.com/timescale/timescaledb)** (21.5k GitHub stars): PostgreSQL extension for time-series. Works with standard PostgreSQL drivers.

### Vector Databases

#### In-process (embedded)
- **[FAISS](https://github.com/facebookresearch/faiss)** (32.5k GitHub stars): Facebook AI Similarity Search. In-process library for efficient similarity search and clustering of dense vectors. CPU and GPU, many index types (flat, IVF, HNSW). No server; use from Python to build and query indices in memory or on disk.
- **[DuckDB](https://github.com/duckdb/duckdb)** (35.6k GitHub stars): In-process analytical DB with vector extension. SQL interface; store and query embeddings alongside tabular data (see In-Memory Analytical Databases).
- **[LanceDB](https://github.com/lancedb/lancedb)** (5.2k GitHub stars): Embedded vector database. Runs in-process like SQLite; no server. Built on Lance (columnar format). Vector search, metadata filtering, multimodal. Good for RAG and LLM apps.
- **[Chroma](https://github.com/chroma-core/chroma)** (14.2k GitHub stars): Vector database with embedded mode. Can run in-process (no server) or as a client to a Chroma server. Persistent or in-memory.
- **[sqlite-vec](https://github.com/asg017/sqlite-vec)** (1.2k GitHub stars): SQLite extension for vector similarity search. In-process, single file. Good for small to medium vector workloads.

#### Server, managed, or client–server
- **[Milvus](https://github.com/milvus-io/milvus)** (30.2k GitHub stars): Open-source vector database. Self-hosted or Zilliz Cloud. Multiple index types (HNSW, IVF, etc.), scalable.
- **[Qdrant](https://github.com/qdrant/qdrant)** (17.2k GitHub stars): Vector database and similarity search engine. Self-hosted or Qdrant Cloud. HNSW, metadata filtering, disk-backed. Python client.
- **[Weaviate](https://github.com/weaviate/weaviate)** (11.2k GitHub stars): Vector database with GraphQL and REST. Self-hosted or Weaviate Cloud. Hybrid search, modules for embeddings and ML.
- **[pgvector](https://github.com/pgvector/pgvector)** (8.5k GitHub stars): PostgreSQL extension for vector similarity search. Use with standard PostgreSQL drivers (e.g. psycopg2). Server-based.
- **[Pinecone](https://www.pinecone.io/)**: Managed vector database (cloud only). Serverless or pod-based. Python client; no self-hosting.
- **[Chroma](https://github.com/chroma-core/chroma)** (14.2k GitHub stars, server mode): Run Chroma as a separate server; connect via client (see In-process for embedded use).

#### Populating vector databases
- **Embeddings**: Generate vectors before or during ingestion. **[sentence-transformers](https://github.com/UKPLab/sentence-transformers)** (16.5k GitHub stars): Local embedding models (e.g. all-MiniLM). **[openai](https://github.com/openai/openai-python)** / **[tiktoken](https://github.com/openai/tiktoken)**: OpenAI embeddings and tokenization. **[Hugging Face Transformers](https://github.com/huggingface/transformers)** (see Deep Learning): General embedding models.
- **Document loaders & chunking**: **[LlamaIndex](https://github.com/run-llama/llama_index)** (46.5k GitHub stars): Document loaders, chunking, and ingestion pipelines for RAG; supports many vector stores (in-process and server). **[LangChain](https://github.com/langchain-ai/langchain)**: Document loaders, text splitters, and vector-store integrations (Chroma, Qdrant, Pinecone, etc.).
- **Batch ingestion**: In-process DBs (LanceDB, Chroma embedded, DuckDB) are populated by adding records from your process. Server DBs (Qdrant, Weaviate, Pinecone, pgvector) are populated via their Python clients; use batching APIs for large datasets. **[ConnectorX](https://github.com/sfu-db/connector-x)** (2.5k GitHub stars, see Data Integration): Load from relational DBs into DataFrames; then embed and write to your vector DB of choice.

### Database Testing & Fixtures
- **[pytest-postgresql](https://github.com/ClearcodeHQ/pytest-postgresql)** (505 GitHub stars): PostgreSQL fixtures for pytest. Isolated test databases.
- **[pytest-mysql](https://github.com/ClearcodeHQ/pytest-mysql)** (56 GitHub stars): MySQL fixtures for pytest.
- **[factory-boy](https://github.com/FactoryBoy/factory_boy)** (3.8k GitHub stars): Test data generation. Works with ORMs for creating test fixtures.


## Data Classes and Validation

- **[Pandera](https://github.com/unionai/pandera)** (4.2k GitHub stars): Data validation and testing.
- **[Pydantic](https://github.com/pydantic/pydantic)** (26.5k GitHub stars): Data validation and parsing.
- **[Hypothesis](https://github.com/HypothesisWorks/hypothesis)** (8.4k GitHub stars): Property-based testing.
- **[Marshmallow](https://github.com/marshmallow-code/marshmallow)** (7.2k GitHub stars): Lightweight library for converting complex objects to and from simple Python datatypes. Object serialization/deserialization.
- **[attrs](https://github.com/python-attrs/attrs)** (5.1k GitHub stars): Classes without boilerplate. The base attrs library that many validation tools build upon.
- **[msgspec](https://github.com/jcrist/msgspec)** (2.2k GitHub stars): Fast serialization and validation library with built-in support for JSON, MessagePack, YAML, and TOML.
- **[Cerberus](https://github.com/pyeve/cerberus)** (3.2k GitHub stars): Lightweight data validation library.
- **[Voluptuous](https://github.com/alecthomas/voluptuous)** (2.1k GitHub stars): Data validation library with a focus on clarity and simplicity.
- **dataclasses**: Built-in (Python 3.7+). Classes with automatically generated special methods. No separate repo.
- **TypedDict**: Built-in (Python 3.8+). Type hints for dictionaries with a fixed set of keys. No separate repo.



## FrontEnds

### Web Frameworks (APIs & Full-Stack)
- **[FastAPI](https://github.com/tiangolo/fastapi)** (94.5k GitHub stars): Modern, high-performance web framework for building APIs with Python. Based on standard Python type hints. Fast development speed, automatic API documentation.
- **[Django](https://github.com/django/django)** (86.6k GitHub stars): The Web framework for perfectionists with deadlines. Full-featured framework with ORM, admin panel, and more. (Note: Django ORM is also listed in Databases section)
- **[Flask](https://github.com/pallets/flask)** (71.1k GitHub stars): The Python micro framework for building web applications. Very popular for APIs and web apps. Minimal and flexible.
- **[Bottle](https://github.com/bottlepy/bottle)** (8.7k GitHub stars): Lightweight web framework. Single-file framework, minimal dependencies.
- **[Tornado](https://github.com/tornadoweb/tornado)** (22.4k GitHub stars): Web framework and asynchronous networking library. Handles long-polling and WebSockets.
- **[Sanic](https://github.com/sanic-org/sanic)** (18.2k GitHub stars): Async web framework. Built for speed, supports async/await.

### Ultra-Lightweight (Minimal Dependencies)
- **[Gradio](https://github.com/gradio-app/gradio)** (41.4k GitHub stars): Very lightweight, perfect for ML demos. Auto-generates UI from function signatures. Minimal code required.
- **[NiceGUI](https://github.com/zauberzeug/nicegui)** (15.1k GitHub stars): Lightweight web UI framework. Simple API, minimal dependencies. Good for dashboards and tools.
- **[JustPy](https://github.com/justpy-org/justpy)** (1.3k GitHub stars): Simple, lightweight web framework. Write Python, get web apps. No HTML/JS knowledge needed.
- **[Solara](https://github.com/widgetti/solara)** (2.2k GitHub stars): React-like framework for Python. Lightweight and fast. Good for interactive data apps.
- **[Reflex](https://github.com/reflex-dev/reflex)** (22.5k GitHub stars): Modern web framework. Lightweight, fast hot-reload. Good for full-stack apps.

### Lightweight (Popular & Easy)
- **[Streamlit](https://github.com/streamlit/streamlit)** (43.2k GitHub stars): Very popular, simple API. Great for data apps and dashboards. Minimal code to get started.
- **[Panel](https://github.com/holoviz/panel)** (5.6k GitHub stars): Lightweight dashboarding. Works with many visualization libraries. Part of HoloViz ecosystem.
- **[Voila](https://github.com/voila-dashboards/voila)** (5.7k GitHub stars): Turn Jupyter notebooks into standalone web apps. Very lightweight wrapper.

### Medium Weight (More Features)
- **[Dash](https://github.com/plotly/dash)** (24.4k GitHub stars): Plotly's framework. More control than Streamlit, but still relatively lightweight. Good for complex dashboards.
- **[Shiny for Python](https://github.com/posit-dev/py-shiny)** (1.7k GitHub stars): R Shiny ported to Python. More features, slightly heavier. Good for interactive apps.

### Desktop GUI (Lightweight Options)
- **Tkinter**: Built into Python. Ultra-lightweight desktop GUI. Simple but functional. (Built-in, no separate repo)
- **PyQt/PySide**: More features than Tkinter, but still relatively lightweight. Professional desktop apps.
- **[Flet](https://github.com/flet-dev/flet)** (15.4k GitHub stars): Build cross-platform apps (desktop, web, mobile) with Python. Lightweight Flutter wrapper.
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** (13.1k GitHub stars): Modern-looking Tkinter. Lightweight wrapper with better styling.

### Terminal UI (Ultra-Lightweight)
- **[Rich](https://github.com/Textualize/rich)** (55.2k GitHub stars): Beautiful terminal output and progress bars. Very lightweight.
- **[Textual](https://github.com/Textualize/textual)** (33.8k GitHub stars): Terminal UI framework. Build interactive terminal apps. Lightweight.
- **[Click](https://github.com/pallets/click)** (17.1k GitHub stars): Command-line interface creation. Minimal dependencies.
- **[cursor](https://github.com/lethargilistic/cursor)** (194 GitHub stars): Terminal cursor control library. Hide or show the terminal cursor. Works on Linux and Windows.

## Linters

### General Code Linters
- **[Ruff](https://github.com/astral-sh/ruff)** (45.4k GitHub stars): Extremely fast Python linter and formatter written in Rust. Can replace Flake8, isort, and many single‑purpose plugins.
- **[Flake8](https://github.com/PyCQA/flake8)** (3.8k GitHub stars): Classic extensible Python style checker. Plugin ecosystem for many additional rules.
- **[Pylint](https://github.com/pylint-dev/pylint)** (5.6k GitHub stars): Comprehensive static code analyzer. Enforces coding standards and detects code smells.

### Type Checkers
- **[mypy](https://github.com/python/mypy)** (20.1k GitHub stars): Static type checker for Python. Enforces type hints at compile time.
- **[Pyright](https://github.com/microsoft/pyright)** (15.1k GitHub stars): Fast, incremental type checker for Python by Microsoft. Great editor integration.

### Security & Docs
- **[Bandit](https://github.com/PyCQA/bandit)** (7.6k GitHub stars): Security linter for Python. Finds common security issues in code.
- **[pydocstyle](https://github.com/PyCQA/pydocstyle)** (1.1k GitHub stars): Docstring style checker. Ensures consistency with PEP 257 and related conventions.

## Misc

### Web Scraping & HTTP
- **[requests](https://github.com/psf/requests)** (53.7k GitHub stars): Simple, elegant HTTP library for Python. Most popular Python HTTP library.
- **[aiohttp](https://github.com/aio-libs/aiohttp)** (16.2k GitHub stars): Async HTTP client/server framework. For async web scraping and API clients.
- **[beautifulsoup4](https://github.com/waylan/beautifulsoup4)** (30k GitHub stars): Web scraping and HTML/XML parsing library. Extract data from HTML and XML files.
- **[scrapy](https://github.com/scrapy/scrapy)** (59.5k GitHub stars): Fast, high-level web crawling and scraping framework. Production-ready web scraping.

### Testing
- **[pytest](https://github.com/pytest-dev/pytest)** (13.5k GitHub stars): The pytest framework makes it easy to write small tests, yet scales to support complex functional testing. Most popular Python testing framework.

### Data Profiling & Quality
- **[ydata-profiling](https://github.com/ydataai/ydata-profiling)** (11.8k GitHub stars): Data profiling and EDA. Comprehensive reports from DataFrames. Automated EDA (Exploratory Data Analysis). Successor to pandas-profiling.

### Data Version Control & MLOps
- **[dvc](https://github.com/iterative/dvc)** (15.3k GitHub stars): Data Version Control - Data versioning and ML experiments. Git-like versioning for data and models.
- **[kedro](https://github.com/kedro-org/kedro)** (10.7k GitHub stars): Toolbox for production-ready data science. Uses software engineering best practices to help create data engineering and data science pipelines that are reproducible, maintainable, and modular.

### Project Management & Templates
- **[cookiecutter](https://github.com/cookiecutter/cookiecutter)** (24.5k GitHub stars): Project templates. Generate projects from cookiecutters (project templates).
- **[poetry](https://github.com/python-poetry/poetry)** (29.5k GitHub stars): Modern dependency management. Dependency resolution and packaging.
- **[pipenv](https://github.com/pypa/pipenv)** (24.5k GitHub stars): Dependency management. Combines pip and virtualenv.
- **[conda](https://github.com/conda/conda)** (6.2k GitHub stars): Package and environment management. Popular in data science for managing environments.
- **[uv](https://github.com/astral-sh/uv)** (77.6k GitHub stars): Extremely fast Python package and project manager by Astral (creators of Ruff). Replaces tools like pip, pip-tools, pipx, poetry, pyenv, and virtualenv.


### Data Compression & Performance
- **Blosc**: Speed-up communication between disk and memory, or memory and cpu by compressing data blocks. May use LZ4, Snappy ZFP, ZSTD, or Blosc2 under the hood.
- **Bodo.ai**: High-performance data processing platform.
