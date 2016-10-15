class boost(Wig):
	tarball_uri = 'http://downloads.sourceforge.net/project/boost/boost/1.59.0/boost_1_59_0.tar.gz'
	git_uri = 'https://github.com/boostorg/boost'
	git_branch = 'boost-1.59.0'
	git_init_submodules = True
	last_release_version = 'v1.59.0'
	supported_features = ['python']
	
	def setup(self):
		self.skip('make')
		self.bootstrap_flags = ['--without-libraries=python']
		
	def switch_python_on(self):
		self.bootstrap_flags = []

	def gen_install_snippet(self):
		return ['./bootstrap.sh ' + ' '.join(self.bootstrap_flags), './b2 %s install %s' % (' '.join(self.make_flags), S.PREFIX_CONFIGURE_FLAG)]	
