
import typing
from dataclasses import dataclass
from Options import DeathLink, Toggle, Range, PerGameCommonOptions

class MedalHunt(Toggle):
	"""Whether you must collect all 5 medal items before the route to the boss opens. Currently disabled"""
	display_name = "Medal Hunt"

class ExtraCheckpoint(Toggle):
	"""Adds a checkpoint at the connection between the grass and snow areas"""
	display_name = "Extra Checkpoint"

class DeathLinkAmnesty(Range):
	"""How many deaths does it take to send a DeathLink"""
	display_name = "Death Link Amnesty"
	range_start = 1
	range_end = 50
	default = 10


@dataclass
class MCVOptions(PerGameCommonOptions):
	medal_hunt: MedalHunt
	extra_checkpoint: ExtraCheckpoint
	death_link: DeathLink
	death_link_amnesty: DeathLinkAmnesty