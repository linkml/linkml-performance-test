RUN = poetry run

SCHEMADIR = src/linkml_performance_test/model

$(SCHEMADIR)/%_dataclasses.py: $(SCHEMADIR)/%.yaml
	$(RUN) gen-python $< > $@
$(SCHEMADIR)/%_pydantic.py: $(SCHEMADIR)/%.yaml
	$(RUN) gen-pydantic $< > $@

$(SCHEMADIR)/%.py: $(SCHEMADIR)/%_dataclasses.py
	cp $< $@

use-pydantic:
	cp $(SCHEMADIR)/obograph_pydantic.py $(SCHEMADIR)/obograph.py
use-dataclasses:
	cp $(SCHEMADIR)/obograph_dataclasses.py $(SCHEMADIR)/obograph.py

switch-to-1_1x:
	touch $(SCHEMADIR)/*yaml ;
	poetry add linkml==1.1.19 ;
	poetry add linkml-runtime==1.1.26 ;
	poetry install ;
	make $(SCHEMADIR)/obograph.py

nb:
	$(RUN) jupyter notebook
