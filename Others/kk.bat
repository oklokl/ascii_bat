@echo off
PowerShell -Command "& {$MediaPlayer = [Windows.Media.Playback.MediaPlayer, Windows.Media, ContentType = WindowsRuntime]::New();$MediaPlayer.Source = [Windows.Media.Core.MediaSource]::CreateFromUri('http://jsh891212.dothome.co.kr/DF/soft_Retro_music.mp3');$MediaPlayer.Play();Start-Sleep -Seconds 12}"
pause