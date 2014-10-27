DIR = ../../static/css
MUJIN_TARGET = mujin.css
MUJIN_SOURCES = \
	bootstrap/bootstrap.css \
	fontawesome/fontawesome.css \
	mujin/mujin.sass.css \

.PHONY: all
all: debug

.PHONY: debug
debug: $(DIR)/$(MUJIN_TARGET)

.PHONY: release
release: $(DIR)/$(MUJIN_TARGET)
	@cat $(MUJIN_TARGET) | sed 's/\/\*!/\/**/g' | yui-compressor --type css > $(DIR)/$(MUJIN_TARGET)

$(DIR)/$(MUJIN_TARGET): $(MUJIN_TARGET)
	@mkdir -p $(DIR)
	@cat $(MUJIN_TARGET) > $(DIR)/$(MUJIN_TARGET)

$(MUJIN_TARGET): $(MUJIN_SOURCES)
	@cat $(MUJIN_SOURCES) > $(MUJIN_TARGET)

%.sass.css: %.sass $(shell find . -type f -iname _\*.sass)
	@cat $< | sass --compass --load-path . > $<.css

.PHONY: clean
clean:
	@find . -iname \*.sass.css -exec rm -f {} \;
	@rm -rf .sass-cache
	@rm -f $(MUJIN_TARGET)
	@rm -rf $(DIR)

