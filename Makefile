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
