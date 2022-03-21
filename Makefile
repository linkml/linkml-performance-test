RUN = poetry run

SCHEMADIR = src/linkml_performance_test/model

$(SCHEMADIR)/%_dataclasses.py: $(SCHEMADIR)/%.yaml
	$(RUN) gen-python $< > $@
$(SCHEMADIR)/%_pydantic.py: $(SCHEMADIR)/%.yaml
	$(RUN) gen-python $< > $@

$(SCHEMADIR)/%.py: $(SCHEMADIR)/%_dataclasses.py
	cp $< $@
