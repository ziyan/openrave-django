DIR = ../../static/js
MUJIN_TARGET = mujin.js
MUJIN_SOURCES = \
	debug.js \
	jquery/jquery.js \
	jquery/jquery.cookie.coffee.js \
	ember/handlebars.js \
	ember/ember.js \
	ember/ember.data.js \
	moment.js \
	bootstrap/bootstrap.js \
	mujin/mujin.coffee.js \
	mujin/mujin.utils.coffee.js \
	mujin/mujin.locale.coffee.js \
	mujin/mujin.user.coffee.js \
	mujin/mujin.robot.coffee.js \

.PHONY: all
all: debug

.PHONY: debug
debug: $(DIR)/$(MUJIN_TARGET)

.PHONY: release
release: $(DIR)/$(MUJIN_TARGET)
	@cat $(MUJIN_TARGET) | sed 's/\/\*!/\/**/g' | yui-compressor --type js > $(DIR)/$(MUJIN_TARGET)

$(DIR)/$(MUJIN_TARGET): $(MUJIN_TARGET)
	@mkdir -p $(DIR)
	@cat $(MUJIN_TARGET) > $(DIR)/$(MUJIN_TARGET)

$(MUJIN_TARGET): $(MUJIN_SOURCES)
	@cat $(MUJIN_SOURCES) > $(MUJIN_TARGET)

%.coffee.js: %.coffee
	@cat $< | coffee -c -s > $<.js

.PHONY: clean
clean:
	@find . -iname \*.coffee.js -exec rm -f {} \;
	@rm -f $(MUJIN_TARGET)
	@rm -rf $(DIR)

