DATA=2014-05-09-baseline-0 \
2014-05-13-baseline-1 \
2014-05-16-drop-0 \
2014-05-16-drop-1

csv:
	for dir in $(DATA); do \
    	cd $$dir ; log2csv logfile-000; cd .. ;\
	done

clean:
	for dir in $(DATA); do \
		rm -f $$dir/*.csv; \
	done
