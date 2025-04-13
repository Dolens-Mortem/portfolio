using BepInEx;
using HarmonyLib;
using System.Collections.Generic;
using System.Reflection.Emit;
using UnityEngine;
using static ClutterSystem;
using static ItemDrop;

namespace AllStarMobs
{
    [BepInPlugin("AllStarMobs.ValheimMod", "AllStarMobs", "1.0.0")]
    [BepInProcess("valheim.exe")]

    public class ValheimMod : BaseUnityPlugin
    {
        private readonly Harmony harmony = new Harmony("AllStarMobs.ValheimMod");

        private void Awake()
        {
            harmony.PatchAll();
        }

        private void OnDestroy()
        {
            harmony.UnpatchSelf();
        }

        [HarmonyPatch]
        class Spawn_Patch : SpawnSystem
        {
            [HarmonyPatch(typeof(SpawnSystem), "Spawn")]

            [HarmonyPrefix]
            public static void Prefix(ref SpawnSystem.SpawnData critter)
            {
                critter.m_maxLevel = (critter.m_maxLevel > 3) ? critter.m_maxLevel : 3;
                critter.m_minLevel = critter.m_maxLevel;
                critter.m_levelUpMinCenterDistance = 0f;
            }
        }

        [HarmonyPatch]
        class SpawnArea_Patch : SpawnArea
        {
            [HarmonyPatch(typeof(SpawnArea), nameof(SpawnArea.GetLevelUpChance))]

            [HarmonyPostfix]
            public static void Postfix(ref float __result)
            {
                __result = 999f;
            }
        }

        [HarmonyPatch]
        class Creature_SPW_Patch : CreatureSpawner
        {
            [HarmonyPatch(typeof(CreatureSpawner), "Spawn")]

            [HarmonyPrefix]
            public static void Prefix(ref int ___m_maxLevel, ref int ___m_minLevel)
            {
                ___m_maxLevel = (___m_maxLevel > 3) ? ___m_maxLevel : 3;
                ___m_minLevel = ___m_maxLevel;
            }
        }

        [HarmonyPatch]
        class Trigger_SPW_Patch : TriggerSpawner
        {
            [HarmonyPatch(typeof(TriggerSpawner), "Spawn")]

            [HarmonyPrefix]
            public static void Prefix(ref int ___m_maxLevel, ref int ___m_minLevel)
            {
                //Debug.Log($"max: {___m_maxLevel}");
                //Debug.Log($"min: {___m_minLevel}");
                ___m_maxLevel = (___m_maxLevel > 3) ? ___m_maxLevel : 3;
                ___m_minLevel = ___m_maxLevel;
                //Debug.Log($"MAX: {___m_maxLevel}");
                //Debug.Log($"MIN: {___m_minLevel}");
            }
        }

        [HarmonyPatch(typeof(Humanoid), "BlockAttack")]
        public static class BlockAttackPatch
        {

            [HarmonyPrefix]
            public static void Prefix(ref HitData hit, ref float ___m_blockTimer, ref float ___m_blockStaminaDrain)
            {
                if (___m_blockTimer < 0.25f)
                {
                    hit.BlockDamage(hit.GetTotalBlockableDamage());
                    ___m_blockStaminaDrain = 0;
                }
            }

            [HarmonyPostfix]
            public static void Postfix(ref float ___m_blockStaminaDrain)
            {
                ___m_blockStaminaDrain = 25f;
            }

        }

    }
}