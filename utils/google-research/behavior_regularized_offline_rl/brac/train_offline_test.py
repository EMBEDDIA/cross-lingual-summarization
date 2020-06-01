# coding=utf-8
# Copyright 2019 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for behavior_regularized_offline_rl.brac.train_offline."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from absl import flags
import tensorflow.compat.v1 as tf
from behavior_regularized_offline_rl.brac import train_offline


class TrainOfflineTest(tf.test.TestCase):

  def test_train_offline(self):
    data_dir = 'testdata/data'
    flags.FLAGS.data_root_dir = os.path.join(flags.FLAGS.test_srcdir, data_dir)
    flags.FLAGS.sub_dir = '0'
    flags.FLAGS.env_name = 'HalfCheetah-v2'
    flags.FLAGS.data_name = 'example'
    flags.FLAGS.agent_name = 'bc'
    flags.FLAGS.gin_bindings = [
        'train_eval_offline.model_params=((200, 200),)',
        'train_eval_offline.optimizers=(("adam", 5e-4),)']
    flags.FLAGS.n_train = 100
    flags.FLAGS.n_eval_episodes = 1
    flags.FLAGS.total_train_steps = 100  # Short training.

    train_offline.main(None)  # Just test that it runs.


if __name__ == '__main__':
  tf.test.main()
