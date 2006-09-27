from sugar.presence import PresenceService
from model.Friends import Friends
from model.MeshModel import MeshModel
from model.Owner import ShellOwner

class ShellModel:
	def __init__(self):
		self._current_activity = None

		PresenceService.start()
		self._pservice = PresenceService.get_instance()

		self._owner = ShellOwner()
		self._owner.announce()
		self._friends = Friends()
		self._mesh = MeshModel()

	def get_mesh(self):
		return self._mesh

	def get_friends(self):
		return self._friends

	def get_invites(self):
		return self._owner.get_invites()

	def get_owner(self):
		return self._owner

	def set_current_activity(self, activity_id):
		self._current_activity = activity_id
		self._owner.set_current_activity(activity_id)

	def get_current_activity(self):
		return self._current_activity
