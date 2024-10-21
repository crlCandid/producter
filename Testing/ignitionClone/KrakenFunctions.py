			
	msg = ''
	found = False
	error = False
	
	error, found, msg = getLaserLocal(aligner_id, logger)
	
	if found:
	    logger.info('Local Found: %s '%(aligner_id))
	    return msg
	    
	if error:
	    logger.warn('Local Search Error : %s \nError: %s'%(aligner_id, msg))
	   
	error, found, msg = getLaserKraken(aligner_id, logger)
	    	
	if found:
		logger.info('Kraken Found: %s '%(aligner_id))
		return msg
		
	if error:
		logger.warn('Kraken Search Error : %s \nError: %s'%(aligner_id, msg))
		return msg