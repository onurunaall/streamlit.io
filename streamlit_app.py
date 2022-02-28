from timeseries_generator import LinearTrend, Generator, WhiteNoise, RandomFeatureFactor
import pandas as pd

lt = LinearTrend(coef=2.0, offset=1., col_name="my_linear_trend")

g: Generator = Generator(factors={lt}, features=None, date_range=pd.date_range(start="01-01-2020", end="01-20-2020"))
g.generate()
g.plot()

wn = WhiteNoise(stdev_factor=0.05)
g.update_factor(wn)
g.generate()
g.plot()

rff = RandomFeatureFactor(feature="my_feature", feature_values=["feature1", "feature2"], min_factor_value=1, max_factor_value=10)
g.update_factor(rff)
g.features = {"my_feature": ["feature1", "feature2"]}
df: pd.DataFrame = g.generate()
print(df.head(5))

df_plot=df.set_index('date')
df_plot[["my_feature", "value"]].pivot(columns=["my_feature"], values="value").plot()

lt2 = LinearTrend(feature="my_feature", feature_values={"feature1": {"coef": 1., "offset": 1.}, "feature2": {"coef": 0.05, "offset": 1.}})

g.update_factor(lt2)
df = g.generate()

df_plot=df.set_index('date')
df_plot[["my_feature", "value"]].pivot(columns=["my_feature"], values="value").plot()
